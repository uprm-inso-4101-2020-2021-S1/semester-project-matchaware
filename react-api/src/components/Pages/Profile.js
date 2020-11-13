import React from 'react'
import Doge from '../doge.jpg'
function Profile() {
    return(
        <React.Fragment>
            <h1>
                Profile
                
            </h1>
            <img src={Doge} alt="He who is doge"/>
            <p>This is the profile. This you. Yea you. Theres nothing here.</p>
        </React.Fragment>
    )
}
export default Profile;