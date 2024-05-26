import React from 'react';


const Indexpage = (props) => {
    React.useEffect(() => {
            props.history.push("/login");
        
        //eslint-disable-next-line
    }, [0])
    return (
        <div>
        </div>
    )
}

export default Indexpage
