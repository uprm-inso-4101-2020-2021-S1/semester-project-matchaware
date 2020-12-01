import React from 'react'
import Container from 'react-bootstrap/Container'
import Button from 'react-bootstrap/Button'
import Form from 'react-bootstrap/Form'
import Card from 'react-bootstrap/Card'
import Col from 'react-bootstrap/Col'
import { setUserSession } from '../../utils/Commons'
import axios from 'axios'
import { useState } from 'react'


export default function SignUp(props) {
    const [user, setUser] = useState({
        firstname: null,
        lastname: null,
        description: null,
        password: null,
        email: null,
        mayor: null,
        interests: null,
        profilepicture: null
    })
    const [error, setError] = useState([])
    const [loading, setLoading] = useState(false)
    // handle button click of login form 
    // should be changed in the future
    const handleSignUp = () => {
        setError(null)
        setLoading(true)
        axios.post(
            `https://5fbb344fc09c200016d4042c.mockapi.io/credentials/currentUser`,
            { firstname: user.firstname, lastname: user.lastname, email: user.email, password: user.password, profilepicture: user.profilepicture })
            .then(response => {
                setLoading(false)
                setUserSession(response.data.id, response.data.email)
                props.history.push('/homepage')
            }).catch(error => {
                setLoading(false)
                if (error.response && error.response.status === 401) setError(error.response.data.message)
                else setError("Something went wrong. Please try again later.")
            })
            
    }
    console.log(user)
    return (
        <Container className='p-5'>
            <Card className="text-center p-4">
                <Card.Title>
                    <h1>
                        Welcome Back, Colegial!
                    </h1>
                </Card.Title>

                <Form>
                    <Form.Row>

                        <Form.Group
                            as={Col}
                            className='p-2'
                            controlId="formFirstName">
                            <Form.Label>
                                First Name:
                            </Form.Label>
                            <Form.Control
                                type="firstname"
                                placeholder="First Name"
                                value={user.firstname}
                                onChange={e => setUser({
                                    firstname: e.target.value,
                                    lastname: user.lastname,
                                    description: user.description,
                                    password: user.password,
                                    email: user.firstname,
                                    mayor: user.mayor,
                                    interests:  user.interests,
                                    profilepicture: user.profilepicture
                                })}
                            />
                        </Form.Group>

                        <Form.Group
                            as={Col}
                            className='p-2'
                            controlId="formLastName">
                            <Form.Label>
                                Last Name:
                                </Form.Label>
                            <Form.Control
                                type="lastname"
                                placeholder="Last Name"
                                value={user.lastname}
                                onChange={e => setUser({
                                    firstname: user.firstname,
                                    lastname: e.target.value,
                                    description: user.description,
                                    password: user.password,
                                    email: user.email,
                                    mayor: user.mayor,
                                    interests:  user.interests,
                                    profilepicture: user.profilepicture
                                })}
                            />
                        </Form.Group>

                    </Form.Row>


                    <Form.Row>

                        <Form.Group
                            as={Col}
                            className='p-2'
                            controlId="formEmail">
                            <Form.Label>
                                Email Address:
                                </Form.Label>
                            <Form.Control
                                type="email"
                                placeholder="Email@service.com"
                                value={user.email}
                                onChange={e => setUser({
                                    firstname: user.firstname,
                                    lastname: user.lastname,
                                    description: user.description,
                                    password: user.password,
                                    email: e.target.value,
                                    mayor: user.mayor,
                                    interests:  user.interests,
                                    profilepicture: user.profilepicture
                                })}
                            />
                            <Form.Text className="text-muted">
                                Your email addresss is in good hands.
                            </Form.Text>
                        </Form.Group>

                        <Form.Group
                            as={Col}
                            className='p-2'
                            controlId="formPassword">
                            <Form.Label>
                                Password:
                                </Form.Label>
                            <Form.Control
                                type="password"
                                placeholder="Password123"
                                value={user.password}
                                onChange={e => setUser({
                                    firstname: user.firstname,
                                    lastname: user.lastname,
                                    description: user.description,
                                    password: e.target.value,
                                    email: user.password,
                                    mayor: user.mayor,
                                    interests:  user.interests,
                                    profilepicture: user.profilepicture
                                })}
                            />
                            <Form.Text>
                                Please use an 8 character long password.
                            </Form.Text>
                        </Form.Group>

                    </Form.Row>

                    <Form.Row>

                        <Form.Group
                            as={Col}
                            className='p-2'
                            controlId="formEmailConfirm">
                            <Form.Label>
                                Confirm Email address:
                            </Form.Label>
                            <Form.Control
                                type="emailConfirm"
                                placeholder="Email@service.com"
                            />
                        </Form.Group>

                        <Form.Group as={Col} className='p-2'>
                            <Form.Label
                                controlId="formPasswordConfirm">
                                Confirm Password:
                            </Form.Label>
                            <Form.Control
                                type="password"
                                placeholder="Password123"
                            />
                        </Form.Group>

                    </Form.Row>

                    <Form.Group>
                        <Form.File
                            id="profilepicture"
                            label="Profile Picture"
                            data-browse="Upload Image"
                            custom
                        />
                    </Form.Group>


                </Form>
                <Button variant="success"
                    onClick={handleSignUp}
                    disabled={loading}
                >
                    Sign Up
                    </Button>
            </Card>
        </Container>
        
    )
}
