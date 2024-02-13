import Contact_form from "./Contact_form";
import './Contact.css'
import Footer from "./Footer";

const Contact = (prpos)=>{
    return(
        <div className="contact_container">
            <div className="contact">
            <Contact_form/>
            <Footer/>
            </div>
            
        </div>
    )
};
export default Contact;