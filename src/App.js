import React, { useState, useEffect} from 'react';
import { BrowserRouter as Router,Route, Switch} from 'react-router-dom';
import Header from './components/Header'
import Profile from './components/Pages/UserProfile'
import Following from './components/Pages/Following'
import Messages from './components/Pages/Messages'
import './App.css'
import Login from './components/Pages/Login'
import SignUp from './components/Pages/SignUp';
import HomePage from './components/Pages/HomePage'
import PrivateRoute from './utils/PrivateRoute'
import PublicRoute from './utils/PublicRoute'
import { getToken, removeUserSession, setUserSession } from './utils/Commons';
import axios from 'axios'
import LandingPage from './components/Pages/Lands/LandingPage'




    export default function App(){
      const [authLoading, setAuthLoading] = useState(true)

      useEffect(() => {
        const token = getToken()
        if (!token){
          return
        }
      axios.get(`https://5fbb344fc09c200016d4042c.mockapi.io/credentials/currentUser/${token}`).then(response => {
    // axios.get(`http://localhost:3000/verifyToken?token=${token}`).then(response => {
      setUserSession(response.data.id, response.data.email)
      setAuthLoading(false)
    }).catch(error => {
      removeUserSession()
      setAuthLoading(false)
    })
  }, [])
 
  if (authLoading && getToken()) {
    return <div className="content">Checking Authentication...</div>
  }

        return (
          <Router>
            <div className="App">
              <Header />
              <Route exact path="/" render={props =>(
                <React.Fragment>
                  <LandingPage />
                </React.Fragment>
              )} /> 

              <Switch>
              <PrivateRoute path="/profile" component={Profile} />
              <PrivateRoute path="/following" component={Following} />
              <PrivateRoute path="/messages" component={Messages} />
              <PrivateRoute path="/homepage" component={HomePage}/>
              <PublicRoute path="/login" component={Login} />
              <PublicRoute path="/signup" component={SignUp}/>
              </Switch>
            </div>
          </Router>
        )
      }
    
