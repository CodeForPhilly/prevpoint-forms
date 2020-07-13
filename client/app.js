import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter, Route } from 'react-router-dom'

import FormMapper, { FormMapperPicker } from './FormMapper'
import Nav from './components/Nav'

const App = () => {
  return (
    <div>
      <BrowserRouter>
        <Nav />
        <Route exact path="/app/form-mapper/" component={FormMapperPicker} />
        <Route path="/app/form-mapper/:img_name/" component={FormMapper} />
      </BrowserRouter>
    </div>
  )
}

ReactDOM.render(<App />, document.querySelector('#react-app'))
