import React from 'react'
import Card from 'react-bootstrap/Card'
import CardDeck from 'react-bootstrap/CardDeck'
import Doge from '../../doge.jpg'

function HotOrganizations(){
    return(
        <div fluid><h1 class="organizationsPresentation">Organizations</h1>
            <CardDeck>
            <Card>
                    <Card.Img variant="top" src= {Doge} />
                        <Card.Body>
                        <Card.Title>Here goes the Org name?</Card.Title>
                            <Card.Text>
                                Org Descriptop?
                            </Card.Text>
                        </Card.Body>
                    <Card.Footer>Creation date</Card.Footer>
                </Card>
                <Card>
                    <Card.Img variant="top" src= {Doge} />
                        <Card.Body>

                    
                            <Card.Title>Here goes the Org name?</Card.Title>
                                <Card.Text>
                                Org Descriptop?
                                </Card.Text>
                        </Card.Body>
                    <Card.Footer>Creation date</Card.Footer>
                </Card>
                <Card>
                    <Card.Img variant="top" src= {Doge} />
                    <Card.Body>

                        <Card.Title>Here goes the Org name?</Card.Title>
                            <Card.Text>
                            Org Descriptop?
                            </Card.Text>
                    </Card.Body>
                    <Card.Footer>Creation date</Card.Footer>
                </Card>
            </CardDeck>
        </div>
    )
}
export default HotOrganizations