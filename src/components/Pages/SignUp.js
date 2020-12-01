import React from 'react'
import Container from 'react-bootstrap/Container'
import Button from 'react-bootstrap/Button'
import Form from 'react-bootstrap/Form'
import Card from 'react-bootstrap/Card'
import Col from 'react-bootstrap/Col'


export default function SignUp() {
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

                        <Form.Group as={Col} className='p-2' controlId="formFirstName">
                            <Form.Label>First Name: </Form.Label>
                            <Form.Control type="firstname" placeholder="First Name" />
                        </Form.Group>

                        <Form.Group as={Col} className='p-2' controlId="formLastName">
                            <Form.Label>Last Name: </Form.Label>
                            <Form.Control type="lastname" placeholder="Last Name" />
                        </Form.Group>

                    </Form.Row>


                    <Form.Row>

                        <Form.Group as={Col} className='p-2' controlId="formEmail">
                            <Form.Label>Email Address:</Form.Label>
                            <Form.Control type="email" placeholder="Email@service.com" />
                            <Form.Text className="text-muted">
                                Your email addresss is in good hands.
                        </Form.Text>
                        </Form.Group>

                        <Form.Group as={Col} className='p-2' controlId="formPassword">
                            <Form.Label>Password:</Form.Label>
                            <Form.Control type="password" placeholder="Password123" />
                            <Form.Text>Please use an 8 character long password.</Form.Text>
                        </Form.Group>

                    </Form.Row>

                    <Form.Row>

                        <Form.Group as={Col} className='p-2' controlId="formEmailConfirm">
                            <Form.Label>Confirm Email address:</Form.Label>
                            <Form.Control type="emailConfirm" placeholder="Email@service.com" />
                        </Form.Group>

                        <Form.Group as={Col} className='p-2'>
                            <Form.Label controlId="formPasswordConfirm"> Confirm Password: </Form.Label>
                            <Form.Control type="password" placeholder="Password123" />
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
                <Button variant="success" >Sign Up</Button>
            </Card>
        </Container>
    )
}
