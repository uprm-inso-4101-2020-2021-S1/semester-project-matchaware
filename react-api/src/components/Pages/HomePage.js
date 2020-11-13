import React from 'react'
import Container from 'react-bootstrap/Container'
import Button from 'react-bootstrap/Button'
import Card from 'react-bootstrap/Card'
import Doge from '../../components/doge.jpg'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'




export default function HomePage() {
  return (

    <Container className="text-center p-5">
      <Row className="justify-content-center">

        <Col xs={7}>

          <Card fluid className="home-picture1 bg-dark text-white">

            <Card.Img variant="top" src={Doge} />
            <Card.ImgOverlay style={{ backgroundImage: 'linear-gradient(rgba(0, 0, 0, 0.5),rgba(0, 0, 0, 0.5))' }}>
              <Card.Title>
                This is a title 1
                    </Card.Title>
              <Card.Text className="align-bottom">
                This will be the description of the image or association related to it.
                    </Card.Text>
              <Button variant="primary">Read More</Button>
            </Card.ImgOverlay>
          </Card>

        </Col>

        <Col xs={5}>

          <Card className="home-picture2 bg-dark text-white">
            <Card.Img variant="top" src={Doge} />
            <Card.ImgOverlay style={{ backgroundImage: 'linear-gradient(rgba(0, 0, 0, 0.5),rgba(0, 0, 0, 0.5))' }}>
              <Card.Title>
                This is a title 2
                    </Card.Title>
              <Card.Text>
                This will be the description of the image or association related to it.
                    </Card.Text>
              <Button variant="primary">Read More</Button>
            </Card.ImgOverlay>
          </Card>
          <br />

          <Card fluid className="home-picture3 bg-dark text-white">
            <Card.Img variant="top" src={Doge} />
            <Card.ImgOverlay style={{ backgroundImage: 'linear-gradient(rgba(0, 0, 0, 0.5),rgba(0, 0, 0, 0.5))' }}>
              <Card.Title>
                This is a title 3
                    </Card.Title>
              <Card.Text>
                This will be the description of the image or association related to it.
                    </Card.Text>
              <Button variant="primary">Read More</Button>
            </Card.ImgOverlay>
          </Card>

        </Col>

      </Row>
      <Container className="p-5">
        <Row>
          <Col md={3}>
                          <div className="cssimg">
                           <img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/3/skyscrapers.jpg" className="img"></img>
                          </div>
                        </Col>
                        <Col>
                          <div className="csstext text-white bg-dark">
                            This is the description of the image.
                          </div>
                        </Col>
        </Row>




      </Container>

    </Container>
  )
}
