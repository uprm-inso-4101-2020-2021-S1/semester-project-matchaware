import React from 'react'
import Card from 'react-bootstrap/Card'
import CardDeck from 'react-bootstrap/CardDeck'
import Doge from '../../doge.jpg'

function HotProject(){
    return(
        <div fluid><h1 class="projectPresentation">Projects</h1>
            <CardDeck>
                <Card>
                    <Card.Img variant="top" src= {Doge} />
                    <Card.Body>

                    
                        <Card.Title>Here goes the Project name?</Card.Title>
                        <Card.Text>
                            Project Description?
                        </Card.Text>
                    </Card.Body>
                    <Card.Footer>Maybe we can put the time when it was posted here</Card.Footer>
                </Card>
                <Card>
                    <Card.Img variant="top" src= {Doge} />
                    <Card.Body>

                    
                        <Card.Title>Here goes the Project name?</Card.Title>
                        <Card.Text>
                            Project Description?
                        </Card.Text>
                    </Card.Body>
                    <Card.Footer>Maybe we can put the time when it was posted here</Card.Footer>
                </Card>
                <Card>
                    <Card.Img variant="top" src= {Doge} />
                    <Card.Body>

                    
                        <Card.Title>Here goes the Project name?</Card.Title>
                        <Card.Text>
                            Project Description?
                        </Card.Text>
                    </Card.Body>
                    <Card.Footer>Maybe we can put the time when it was posted here</Card.Footer>
                </Card>
            </CardDeck>
        </div>
        
        
    )
}
export default HotProject