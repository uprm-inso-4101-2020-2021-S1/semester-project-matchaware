import React from 'react';
import { BrowserRouter as Router,Route} from 'react-router-dom';
import Header from './components/Header'
import Profile from './components/Pages/Profile'
import Following from './components/Pages/Following'
import Messages from './components/Pages/Messages'
import './App.css'
import LoginAndSignup from './components/Pages/Login'
import SignUp from './components/Pages/SignUp';
import HomePage from './components/Pages/HomePage'



    export default function App(){
        return (
          <Router>
            <div className="App">
              <Header />
              <Route exact path="/" render={props =>(
                <React.Fragment>
                  <HomePage />
                </React.Fragment>
              )} />  

              <Route path="/profile" component={Profile} />
              <Route path="/following" component={Following} />
              <Route path="/messages" component={Messages} />
              <Route path="/login" component={LoginAndSignup} />
              <Route path="/signup" component={SignUp}/>
            </div>
          </Router>
        )
      }
    