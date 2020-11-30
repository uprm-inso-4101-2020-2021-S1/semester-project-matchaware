import React, { useState } from 'react'
import Container from 'react-bootstrap/esm/Container'
import Doge from '../doge.jpg'
import Tabs from 'react-bootstrap/Tabs'
import Tab from 'react-bootstrap/Tab'
import Card from 'react-bootstrap/esm/Card'
import Button from 'react-bootstrap/Button'
import {getUser, getToken} from '../../utils/Commons'
import axios from 'axios'
import { useEffect } from 'react'

function UserProfile() {
    console.log(getUser())
    console.log(getToken())

    const [user,setUser] = useState ({
        firstname: null, 
        lastname: null,
        description: null,
        email: null,
        mayor: null,
        interests: null
     })
    const id = sessionStorage.getUser
    const [error,setError] = useState([])
    const url = v
    useEffect(() => {
        axios.get(url).then(response => 
            setUser({
                firstname : response.data.firstname,
                lastname: response.data.lastname,
                description: response.data.description,
                email: response.data.email,
                mayor: response.data.mayor,
                interests: response.data.interests
            })
        
            ).catch(
                error => {
                    if (error.response && error.response.status === 401) setError(error.response.data.message)
                    else setError("Something went wrong. Please try again later.")
                }
            )
    })


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
                                            Name: {user.firstname} {user.lastname}
                                        </div>
                                </Container>

                                <Container>
                                        <div className="namebox">
                                            Description
                                        </div>
                                        <br/>
                                        <div className="profileTextBox">
                                            {user.description}
                                            {/* {props.user.description} */}
                                        </div>
                                        <br/>
                                        <div className ="namebox">
                                            Email: {user.email}
                                        </div>
                                        <br/>
                                        <div className="namebox">
                                            Mayor: {user.mayor}
                                        </div>
                                        <br/>
                                        <div className="profileTextBox2">
                                            Interests
                                        </div>
                                        <div className="profileTextBox3">
                                            {user.interests}
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
export default UserProfile;