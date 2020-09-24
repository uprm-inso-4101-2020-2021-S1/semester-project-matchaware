import React, { Component } from 'react';
import { BrowserRouter as Router,Route} from 'react-router-dom';
import Topbar from './components/Topbar'
import Header from './components/Header'
import Profile from './components/Pages/Profile'
import Following from './components/Pages/Following'
import Messages from './components/Pages/Messages'



    class App extends Component {

      //need:
      //Buttons with text
      //Images with text and on click animations
      //header
      //another type of image with text at bottom
      //a differnt type of button with text
      //a category filtering button (maybe)
      //side scrolling? (maybe)

    render() {
        return (
          <Router>
            <div className="App">
              <Topbar />
              <Header />
              <Route exact path="/" render={props =>(
                <React.Fragment>
                  <h1>
                    There will be pictures here.
                  </h1>
                </React.Fragment>
              )} />
              <Route path="/profile" component={Profile} />
              <Route path="/following" component={Following} />
              <Route path="/messages" component={Messages} />
            </div>
          </Router>
         
        )
      }
    }


    export default App;