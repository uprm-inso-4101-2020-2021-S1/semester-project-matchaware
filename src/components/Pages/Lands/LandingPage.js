import React from 'react'
import { Button, Col } from 'react-bootstrap'
import { Link } from "react-router-dom";
import '../../../App.css'
import Doge from '../../doge.jpg'
import Form from 'react-bootstrap/Form'
import HotProject from './HotProject'
import HotOrganizations from './HotOrganizations'


function LandingPage() {
    return (
        <div fluid>
            <Form.Row>
                <Col>
                    <div class="presentation">
                        <h1>
                            Uniting our students!
                        </h1>
                        <p>
                            The place to access centralized information about
                            <p>
                                projects, organization and more!
                                <p>
                                    From our beloved <strong>Colegio!</strong>
                                </p>
                            </p>
                        </p>
                    </div>
                    <div class="buttonLandingPage">
                    <Link to="/signup"><Button variant="dark" active>Joing Now</Button> </Link>
                    </div>
                </Col>
                <Col class="dogo">
                    <div><img src={Doge} className="img"></img></div>
                </Col>
            </Form.Row>
            <div class="moti">

                <p>
                    Are you a first year student? Ready to eat the world, but don't know how?
                   <p>
                        Do you want to contribute and grow, but have no one to help?
                           <p>
                            Look no further, we can help you find your team!
                               <p>
                                Join Beyond Horizons today, and expand your scope beyond all you've ever known!
                               </p>
                        </p>

                    </p>
                </p>

            </div>
            <React.Fragment><HotProject/></React.Fragment>
            <React.Fragment><HotOrganizations/></React.Fragment>
        </div>
        
    )
}

export default LandingPage