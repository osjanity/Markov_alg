import React from 'react';
import {FormControl, InputGroup, FormGroup, ControlLabel, HelpBlock, Checkbox, Radio, Button} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.css';




class Input extends React.Component{

    render() {
        return (
          <form className="container" onSubmit={
                (event) => {
                  event.preventDefault();
                  event.stopPropagation();
                  fetch('http://localhost:5000/id', { method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({"x":"y"}) } )
              }
            } >
            <input type="submit"/>

            <InputGroup className="mb-3">
              <InputGroup.Prepend>
                <InputGroup.Text id="basic-addon1">Number of vertices</InputGroup.Text>
              </InputGroup.Prepend>
              <FormControl
                placeholder=""
                aria-label=""
                aria-describedby="basic-addon1"
              />
            </InputGroup>


            <InputGroup className="mb-3">
              <InputGroup.Prepend>
                <InputGroup.Text id="basic-addon1">Edges</InputGroup.Text>
              </InputGroup.Prepend>
              <FormControl
                aria-label=""
                aria-describedby="basic-addon1"
              />
            </InputGroup>


            <InputGroup className="mb-3">
              <InputGroup.Prepend>
                <InputGroup.Text id="basic-addon1">Conditional Probabilities</InputGroup.Text>
              </InputGroup.Prepend>
              <FormControl
                aria-label=""
                aria-describedby="basic-addon1"
              />
            </InputGroup>


            <InputGroup className="mb-3">
              <InputGroup.Prepend>
                <InputGroup.Text>Query: P(</InputGroup.Text>
              </InputGroup.Prepend>
              <FormControl
                aria-label="such as P(X1|X2)"
              />
              <InputGroup.Append>
                <InputGroup.Text>)</InputGroup.Text>
              </InputGroup.Append>
            </InputGroup>

          </form>

        )
    }

}

export default Input;
