import React from 'react'
import Container from 'react-bootstrap/Container'
import Button from 'react-bootstrap/Button'
import Form from 'react-bootstrap/Form'
import Card from 'react-bootstrap/Card'


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

                    <Form.Group className='p-2' controlId="formEmail"> 
                        <Form.Label>Username: </Form.Label>
                        <Form.Control type="email" placeholder="Email@service.com"/>
                        <Form.Text className="text-muted"> 
                            Your email addresss is in good hands.
                        </Form.Text>
                    </Form.Group>

                    <Form.Group controlId="formEmailConfirm">
                            <Form.Label>Confirm Email address:</Form.Label>
                            <Form.Control type="emailConfirm" placeholder="Email@service.com"/>
                    </Form.Group>

                    <Form.Group controlId="formPassword">
                        <Form.Label>Password:</Form.Label>
                        <Form.Control type="Password" placeholder="Password123"/> 
                        <Form.Text>Please use an 8 character long password.</Form.Text>
                    </Form.Group>

                    <Form.Group>
                        <Form.Label controlId="formPasswordConfirm"> Confirm Password: </Form.Label>
                        <Form.Control type="Password" placeholder="Password123"/> 
                    </Form.Group>


                </Form>
                <Button variant="success" >Sign Up</Button>
            </Card>
        </Container>
    )
}
