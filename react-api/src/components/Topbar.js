import React from 'react';
import {Link} from 'react-router-dom';

function Topbar (){
    return(
        <header style = {barStyle}>
            <Link style= {linkStyle} to="/">Home</Link>
            <Link style= {linkStyle}to="/profile">Profile</Link>
            <Link style= {linkStyle}to="/following">Following</Link>
            <Link style= {linkStyle}to="/messages">Messages</Link>
        </header>
    )
}

const barStyle ={
    color:'#000000',
    textDecoration: 'none',
    textAlign: 'center',
    padding: '20px',
    fontFamily: 'Times New Roman',
    fontSize: '20px'
}
const linkStyle={
    color:'#000000',
    padding:'40px'
}

export default Topbar;