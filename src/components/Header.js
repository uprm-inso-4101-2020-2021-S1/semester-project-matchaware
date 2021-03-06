import React from 'react';
import Container from 'react-bootstrap/container'
import Button from 'react-bootstrap/Button'
import Nav from 'react-bootstrap/Nav'
import Navbar from 'react-bootstrap/Navbar'
import Form from 'react-bootstrap/Form'
import FormControl from 'react-bootstrap/FormControl'
import Col from 'react-bootstrap/esm/Col';
import Row from 'react-bootstrap/esm/Row';

function Header (){
    return(
        <Container fluid>
            
            <Navbar className="navBar" expand="lg" variant="dark">
              <Navbar.Brand href="#home">MachaWare</Navbar.Brand>
              <Navbar.Toggle aria-controls="basic-navbar-nav" />
              <Navbar.Collapse id="basic-navbar-nav">
             <Nav className="mr-auto">
              <Nav.Link href="/">Home</Nav.Link>
              <Nav.Link href="/profile">Profile</Nav.Link>
              <Nav.Link href="/following">Following</Nav.Link>
              <Nav.Link href="/messages">Messages</Nav.Link>
              <Nav.Link href="/login">Login</Nav.Link>
              <Nav.Link href="/signup">Signup</Nav.Link>
             </Nav>

            <Form inline>
              <FormControl type="text" placeholder="Search" className="mr-sm-2" />
              <Button variant="outline-success">Search</Button>
            </Form>
            </Navbar.Collapse>
            </Navbar>
        
        <header style={headerStyle}> 
            <h1>
                Beyond Horizon
            </h1>
            <p style={headerStyle2}>
                Connecting our peers
            </p>
        </header>
        </Container>
        
    )
}

const headerStyle = {
    background: '#69bf64',
    color: '#000000',
    textAlign: 'center',
    padding: '20px'
}

const headerStyle2 = {
    color:'#FFFFFF',
    textAlign: 'center'
    
}

export default Header;