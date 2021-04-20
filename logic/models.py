import logging
from abc import ABC
from abc import abstractmethod
from typing import Tuple

import transformers
import tensorflow as tf
from tensorflow.keras import layers

logger = logging.getLogger('absa.model')


class ABSClassifier(tf.keras.Model, ABC):

    @abstractmethod
    def call(
            self,
            token_ids: tf.Tensor,
            attention_mask: tf.Tensor = None,
            token_type_ids: tf.Tensor = None,
            training: bool = False,
            **bert_kwargs
    ) -> Tuple[tf.Tensor, Tuple[tf.Tensor, ...], Tuple[tf.Tensor, ...]]:

def force_to_return_details(kwargs: dict):
    condition = not kwargs.get('output_attentions', False) or \
                not kwargs.get('output_hidden_states', False)
    if condition:
        logger.info('Model should output attentions and hidden states.')
    kwargs['output_attentions'] = True
    kwargs['output_hidden_states'] = True


class BertABSCConfig(transformers.BertConfig):

    def __init__(self, num_polarities: int = 3, **kwargs):
        force_to_return_details(kwargs)
        super().__init__(**kwargs)
        self.num_polarities = num_polarities


class BertABSClassifier(ABSClassifier, transformers.TFBertPreTrainedModel):

    def __init__(self, config: BertABSCConfig, **kwargs):
        super().__init__(config, **kwargs)
        self.bert = transformers.TFBertMainLayer(
            config, name="bert")
        initializer = transformers.modeling_tf_utils.get_initializer(
            config.initializer_range)
        self.dropout = layers.Dropout(config.hidden_dropout_prob)
        self.classifier = layers.Dense(
            config.num_polarities,
            kernel_initializer=initializer,
            name='classifier'
        )

    def call(
            self,
            token_ids: tf.Tensor,
            attention_mask: tf.Tensor = None,
            token_type_ids: tf.Tensor = None,
            training: bool = False,
            **bert_kwargs
    ) -> Tuple[tf.Tensor, Tuple[tf.Tensor, ...], Tuple[tf.Tensor, ...]]:
        outputs = self.bert(
            inputs=token_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
            training=training,
            **bert_kwargs
        )
        sequence_output, pooled_output, hidden_states, attentions = outputs
        pooled_output = self.dropout(pooled_output, training=training)
        logits = self.classifier(pooled_output)
        return logits, hidden_states, attentions
