import React from 'react';

function Header (){
    return(
        <header style={headerStyle}> 
            <h1>
                Beyond Horizon
            </h1>
            <p style={headerStyle2}>
                Connecting our peers
            </p>
        </header>
    )
}

const headerStyle = {
    background: '#69bf64',
    color: '#000000',
    textAlign: 'center',
    padding: '20px'
}

const headerStyle2 = {
    color:'#D3D3D3',
    textAlign: 'center'
    
}

export default Header;