import React from 'react';
import {FormControl, InputGroup, FormGroup, ControlLabel, HelpBlock, Checkbox, Radio, Button} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.css';

type Vertex = string

type Edge = {
  "parent": string,
  "child": string,
  "pcgpe1": number,
  "pcgpe0": number
}

type ComponentState = {
  vertices: Vertex[],
  edges: Edge[]
}

const initialState: ComponentState = {
  vertices: [],
  edges: [],
}

class SpecifierForm extends React.Component {
  constructor(props) {
    super(props);

    this.state = initialState;

    this.handleChange_vertices = this.handleChange_vertices.bind(this);
    this.handleChange_edges = this.handleChange_edges.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }


  handleChange_vertices(event) {
    this.setState({vertices: [...this.state.vertices, event.target.value]});
  }
  handleChange_edges(event) {
    this.setState({edges: [...this.state.edges, event.target.value]});


  handleSubmit(event)
    event.preventDefault();

    const requestBody=
      JSON.stringify({
        // Just encode the MF dag, bro.
      })

    // fetch request
    fetch("/result", {
         method:"POST",
         cache: "no-cache",
         headers:{
             "content_type":"application/json",
         },
         body:requestBody
         }
     ).then(response => {
     return response.json()
    })

  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
          <label>
            Add vertex:
            <input
              type="string"
              value={this.state.vertex}
              onChange={this.handleChange_vertices} />
          </label>
          <input type="submit" value="Submit" />
      </form>,

      <form onSubmit={this.handleSubmit}>
      <label>
        Add edge:
        <input
          type="string"
          value={this.state.edges}
          onChange={this.handleChange_edges} />
      </label>
          <input type="submit" value="Submit" />
      </form>


    );
  }
}


export default SpecifierForm;
