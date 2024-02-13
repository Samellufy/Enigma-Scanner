import Contact_form from './Contact_form'
import Footer from './Footer'
import './Home.css'
import ImgSlider from './ImageSlider'
import Introduction from './Introdcution'
import Viewers from './Viewers'

const Home = (props)=>{
    return (
        <div className="container">
            <ImgSlider/>
            <Viewers/>
            <Introduction/>
            <Contact_form/>
            <Footer/>
        </div>
    )
}
export default Home;