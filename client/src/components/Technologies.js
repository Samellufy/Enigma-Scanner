import './Technologies.css';
const Technology = (props)=>{
    return(
        <div className="tech_content">
            <div className="tech_hw_content">
            <img src="/images/Vectort&h2.png" alt="technologies and hardware"/>
            </div>
            <div className='tech_name_content'>
                <div className='tect_wrap_content'>
                    <img src='/images/python.png' alt='Python'/>
                    <h1>Python</h1>
                </div>
                <div className='tect_wrap_content'>
                    <img src='/images/react.png' alt='Python'/>
                    <h1>React Js</h1>
                </div>
                <div className='tect_wrap_content'>
                    <img src='/images/firebase.png' alt='Python'/>
                    <h1>Firebase</h1>
                </div>
                <div className='tect_wrap_content'>
                    <img src='/images/node.png' alt='Python'/>
                    <h1>Node Js</h1>
                </div>
            </div>
        </div>
    )
}
export default Technology;