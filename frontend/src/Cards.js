import React from 'react';
import {Card, CardGroup} from 'react-bootstrap';
import Input from './Input.js';
import NetworkProps from './Network.js';
import 'bootstrap/dist/css/bootstrap.css';


class Cards extends React.Component{

    render() {
        return (
          <div class="container">
            <CardGroup>
              <Card>
                <Card.Body>
                  <Input/>
                  <Card.Text>
                    Placeholder for probability table before transformation.{' '}
                  </Card.Text>
                </Card.Body>
              </Card>
              <Card>
                <Card.Body>
                  <NetworkProps height={400} width={400} />
                  <Card.Text>
                    Placeholder for probability table after transformation.{' '}
                  </Card.Text>
                </Card.Body>
              </Card>

            </CardGroup>
          </div>

        )
    }

}

export default Cards;
