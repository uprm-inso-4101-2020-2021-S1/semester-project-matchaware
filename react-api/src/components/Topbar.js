import React from 'react';
import {Link} from 'react-router-dom';

function Topbar (){
    return(
        <header>
            |<Link style ={linkStyle}to="/">Home</Link>|
            <Link style ={linkStyle}to="/profile">Profile</Link>|
            <Link style ={linkStyle}to="/following">Following</Link>|
            <Link style ={linkStyle}to="/messages">Messages</Link>|
        </header>
    )
}

const linkStyle ={
    color:'#000000',
    textDecoration: 'none',
    textAlign: 'center'
}
export default Topbar;