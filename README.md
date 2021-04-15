## Clone the repo using
```git clone https://github.com/shivang16/aspect-based-opinion-summarization.git```
``` cd aspect-based-opinion-summarization```

## Install pip linux
```sudo apt install python3-pip```
## Install requirements
```pip3 install -r requirements.txt```

## Install spacy en_core_wb_sm
```python3 -m spacy download en_core_web_sm```


## Install virtual enviroment
```pip3 install virtualenv```
## Activate virtual enviroment
```source venv/bin/activate```

## Install flask
```pip install Flask```

## Download additional nltk packages
```python3 downloads.py```

## Run server
```python3 app.py```


# For getting aspects use

```/get-aspects```

Request
body: 
    {
	"reviews":[
		{
			"header":"Good mobile",
			"text":"This is a very good mobile with awesome features",
			"upvotes":10,
			"rating":4
		},
		{
			"header":"Camera quality is average",
			"text":"Camera quality is not upto the expectation. Apart from that descent mobile phone",
			"upvotes":7,
			"rating":3
		},
		{
			"header":"Very bad performance. Below average speed",
			"text":"I purchased this phone 2 months back and now it is able to run simple applications properly. Phone is not upto the expectations. Worst performance. Bad performance. Unpleasant performance",
			"upvotes":100,
			"rating":1
		},
		{
			"header":"Best mobile",
			"text":"Redmi Note 8 pro is one of the best phone in the market right now. It is value for money with so many different features. I really loved the colous Redmi is providing",
			"upvotes":12,
			"rating":5
		}
	],
	"file_name":"temp"
}

Response:
{"0":"performance","1":"phone","2":"mobile","3":"feature","4":"quality","5":"upto","6":"expectation","7":"Camera","8":"descent","9":"speed","10":"purchase","11":"month","12":"application","13":"market","14":"right","15":"value","16":"money"}


# For getting summary use

```/get-summary```
Request
body: 
    {
	"aspects":[
		"Camera","speed","performance","mobile"
	],
	"file_name":"temp"
    }

Response:
{
    "final_rating": 2.8219736507485305,
    "ratings": {
        "Camera": 3,
        "mobile": 3,
        "performance": 3,
        "speed": 2.2878946029941227
    },
    "summary": "Very bad performance. Below average speed. I purchased this phone 2 months back and now it is able to run simple applications properly. Phone is not upto the expectations. Worst performance. Bad performance. Unpleasant performance. Camera quality is average. Camera quality is not upto the expectation. Apart from that descent mobile phone. Best mobile. Redmi Note 8 pro is one of the best phone in the market right now. It is value for money with so many different features. I really loved the colous Redmi is providing"
}

Graph-> remaining


