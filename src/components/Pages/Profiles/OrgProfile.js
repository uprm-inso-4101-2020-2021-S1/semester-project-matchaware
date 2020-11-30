import React from 'react'
import Container from 'react-bootstrap/esm/Container'
import Doge from '../doge.jpg'
import Tabs from 'react-bootstrap/Tabs'
import Tab from 'react-bootstrap/Tab'
import Card from 'react-bootstrap/esm/Card'
import Button from 'react-bootstrap/Button'

function OrgProfile() {
    return (
        <React.Fragment>
            <Container className="p-5">
                <Card className="bg-light p-4">
                    <Tabs defaultActiveKey="Info" id="uncontrolled-tab-example">
                        <Tab eventKey="Info" title="Info">
                            <hr/>

                            <Container className="profileBox">
                                <Container>
                                    <Card className="profileImg">
                                            <Card.Img variant="top" src={Doge} />
                                        </Card>
                                            <br/>
                                        <div className="namebox">
                                            Name:
                                        </div>
                                </Container>

                                <Container>
                                        <div className="namebox">
                                            Description
                                        </div>
                                        <br/>
                                        <div className="profileTextBox">
                                            Description goes here
                                        </div>
                                        <br/>
                                        <div className ="namebox">
                                            Email:
                                        </div>
                                        <br/>
                                        <div className="namebox">
                                            Fields:
                                        </div>
                                        <br/>
                                        <div className="profileTextBox2">
                                            Looking For
                                        </div>
                                        <div className="profileTextBox3">
                                            ICOM INEL ININ
                                        </div>
                                </Container>

                            </Container>
                           
                        </Tab>
                        <Tab eventKey="Affiliations" title="Affiliations">
                            <hr/>
                            <Container className="profileBox">

                            <Card className="affiliationCard">
                                <Card.Img variant="top" src={Doge}/>
                                <Card.Body>
                                    <Card.Title> Org Name</Card.Title> 
                                    <Card.Text>
                                        Description of the organization or project
                                    </Card.Text>
                                    <Button variant="outline-info">See More</Button>
                                </Card.Body>
                            </Card>

                            <Card className="affiliationCard">
                                <Card.Img variant="top" src={Doge}/>
                                <Card.Body>
                                    <Card.Title> Org Name</Card.Title> 
                                    <Card.Text>
                                        Description of the organization or project
                                    </Card.Text>
                                    <Button variant="outline-info">See More</Button>
                                </Card.Body>
                            </Card>

                            <Card className="affiliationCard">
                                <Card.Img variant="top" src={Doge}/>
                                <Card.Body>
                                    <Card.Title> Org Name</Card.Title> 
                                    <Card.Text>
                                        Description of the organization or project
                                    </Card.Text>
                                    <Button variant="outline-info">See More</Button>
                                </Card.Body>
                            </Card>
                            </Container>
                        </Tab>
                    </Tabs>
                </Card>


            </Container>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
            <br/>
        </React.Fragment>
    )
}
export default Profile;