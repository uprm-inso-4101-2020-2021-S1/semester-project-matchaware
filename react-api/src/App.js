import React from 'react';
import { BrowserRouter as Router,Route} from 'react-router-dom';
import Header from './components/Header'
import Profile from './components/Pages/Profile'
import Following from './components/Pages/Following'
import Messages from './components/Pages/Messages'
import Doge from './components/doge.jpg'
import './App.css'
import Container from 'react-bootstrap/Container'
import Button from 'react-bootstrap/Button'
import Card from 'react-bootstrap/Card'
import LoginAndSignup from './components/Pages/Login'
import SignUp from './components/Pages/SignUp';



    export default function App(){
        return (
          <Router>
            <div className="App">
              <Header />
              <Route exact path="/" render={props =>(
                <React.Fragment>
                  <Container fluid className="p-5">
                 <Card border="success" className="text-center" style={{ width: '40rem'}}>
                   <Card.Header>ICOM</Card.Header>
                   <Card.Img varitant="top"src={Doge}/>
                   <Card.Body>
                    <Card.Title>
                      This is a title
                    </Card.Title>
                    <Card.Text>
                     This will be the description of the image or association related to it.
                    </Card.Text>
                    <Button variant="primary">Read More</Button>
                   </Card.Body>
                 </Card>
                 </Container>
                </React.Fragment>
              )} />  

              <Route path="/profile" component={Profile} />
              <Route path="/following" component={Following} />
              <Route path="/messages" component={Messages} />

              {/*  Delete the following two paths once testiing is complete or the user states have been created. */}
              <Route path="/login" component={LoginAndSignup} />
              <Route path="/signup" component={SignUp}/>
              {/* Read previous comment */}
            </div>
          </Router>
        )
      }
    