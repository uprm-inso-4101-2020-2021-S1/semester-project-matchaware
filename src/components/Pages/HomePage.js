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
              <Button variant="outline-info">Read More</Button>
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
              <Button variant="outline-info">Read More</Button>
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
              <Button variant="outline-info">Read More</Button>
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
            "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"
                <Button variant="outline-info" block>Read More</Button>
            </div>
          </Col>
        </Row>

        <Row>
          <Col md={3}>
            <div className="cssimg">
              <img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/3/skyscrapers.jpg" className="img"></img>
            </div>
          </Col>
          <Col>
            <div className="csstext text-white bg-dark">
            "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"
                <Button variant="outline-info" block>Read More</Button>
            </div>
          </Col>
        </Row>

        <Row>
          <Col md={3}>
            <div className="cssimg">
              <img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/3/skyscrapers.jpg" className="img"></img>
            </div>
          </Col>
          <Col>
            <div className="csstext text-white bg-dark">
            "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"
                <Button variant="outline-info" block>Read More</Button>
            </div>
          </Col>
        </Row>

        <div className="p-5">
        <Button variant="info" size="lg" className="t-5">Load More</Button>
        </div>

      </Container>

    </Container>
  )
}
