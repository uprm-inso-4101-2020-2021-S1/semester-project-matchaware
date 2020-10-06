import React from 'react'
import Container from 'react-bootstrap/Container'
import Button from 'react-bootstrap/Button'
import Form from 'react-bootstrap/Form'
import Card from 'react-bootstrap/Card'



export default function LoginAndSignup() {
    return (
        <Container className='p-5'>
            <Card className="text-center p-4">
                <Card.Title>
                    <h1>
                    Welcome Back, Colegial!
                    </h1>
                </Card.Title>
                
                <Form>

                    <Form.Group
                        controlId="formEmail"> 
                        <Form.Label>Email Address</Form.Label>
                        <Form.Control type="email" placeholder="Username or email"/>
                    </Form.Group>

                    <Form.Group>
                        <Form.Label>
                            Password:
                        </Form.Label>
                        <Form.Control type="password" placeholder="Password123"/> 
                        <Form.Text>
                            Please use an 8 character long password.
                        </Form.Text>
                    </Form.Group>

                </Form>
                
                <Button variant="success" >Login</Button>
            </Card>
        </Container>
    )
}
