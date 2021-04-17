import {createContext} from "react";

interface attributeContext {
  attrs: Array<string>;
  setAttrs: (attrs: Array<string>) => void;
}

const attributeContext = createContext<attributeContext>({
  attrs: [],
  setAttrs: () => {}
});

export default attributeContext;