import './Viewers.css';
const Viewers = (props) =>{
    return (
        <div className="viewers">
            <div className='view_wrap'>
                <a href='https://portswigger.net/web-security/sql-injection'>
               <img src='/images/VectorSQLI.png' alt=''/>
               </a>
            </div>
            <div className='view_wrap'>
                <a href='https://www.loginradius.com/blog/engineering/http-security-headers/'>
                <img src='/images/Vectorsecurity_headers.png' alt=''/>
                </a>
            </div>
            <div className='view_wrap'>
            <a href='https://portswigger.net/web-security/file-path-traversal'>
                <img src='/images/Vectorpath_traversal.png' alt=''/>
                </a>
            </div>
            <div className='view_wrap'>
                <a href='https://portswigger.net/web-security/information-disclosure'>
                <img src='/images/Vectorinformation_disclosure.png' alt=''/>
                </a>
            </div>
        </div>
    )
}
export default Viewers;