import React, { useState } from 'react'
import Container from 'react-bootstrap/Container'
import Button from 'react-bootstrap/Button'
import Form from 'react-bootstrap/Form'
import Card from 'react-bootstrap/Card'
import axios from 'axios'
import { setUserSession } from '../../utils/Commons'



export default function Login(props) {
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("") 
    const [error, setError] = useState([])
    const [loading, setLoading] = useState(false)
   
    // handle button click of login form 
    // should be changed in the future
    const handleLogin = () => {
        setError(null)
        setLoading(true)
        axios.post(
            'https://5fb1b0c987ed490016ea80a8.mockapi.io/test/1/users', 
            { username: username, password: password})
        .then(response => {
            setLoading(false)
            setUserSession(response.data.token, response.data.user)
            props.history.push('/dashboard')
        }).catch(error => {
            setLoading(false)
            if (error.response && error.response.status === 401) setError(error.response.data.message)
            else setError("Something went wrong. Please try again later.")
        })
    }


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
                        controlId="formEmail" > 
                        <Form.Label>Email Address</Form.Label>
                        <Form.Control 
                        value={username} 
                        type="email" 
                        placeholder="Username or email"
                        onChange={e => setUsername(e.target.value)}
                        />
                    </Form.Group>

                    <Form.Group>
                        <Form.Label>
                            Password:
                        </Form.Label>
                        <Form.Control 
                        value={password}
                        type="password"
                        placeholder="Password123"
                        onChange={e => setPassword(e.target.value)}
                        /> 
                        <Form.Text>
                            Please use an 8 character long password.
                        </Form.Text>
                    </Form.Group>

                </Form>
                
                <Button variant="success" value={loading ? 'Loading...' : 'Login'} onClick={handleLogin} disabled={loading}>Login</Button>
            </Card>
        </Container>
    )
}
