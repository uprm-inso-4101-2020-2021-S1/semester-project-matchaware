import React from 'react';
import { Route, Redirect } from 'react-router-dom';
import { getToken } from './Commons';
 
// handle the private routes
export default function PrivateRoute({ component: Component, ...rest }) {
  return (
    <Route
      {...rest}
      render={(props) => getToken() ? <Component {...props} /> : <Redirect to={{ pathname: '/login', state: { from: props.location } }} />}
    />
  )
}
 
