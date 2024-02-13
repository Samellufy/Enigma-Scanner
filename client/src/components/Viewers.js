import './Viewers.css';
const Viewers = (props) =>{
    return (
        <div className="viewers">
            <div className='view_wrap'>
               <img src='/images/VectorSQLI.png' alt=''/>
            </div>
            <div className='view_wrap'>
                <img src='/images/Vectorsecurity_headers.png' alt=''/>
            </div>
            <div className='view_wrap'>
                <img src='/images/Vectorpath_traversal.png' alt=''/>
            </div>
            <div className='view_wrap'>
                <img src='/images/Vectorinformation_disclosure.png' alt=''/>
            </div>
        </div>
    )
}
export default Viewers;