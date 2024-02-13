import './Contact_form.css';
const Contact_form = (props)=>{
    return(
        <div className="contact_form">
            <div className="contact_form_h">
                <h1>JOIN ENIGMA</h1>
                <hr></hr>
                <p>Let's Secure Your website Together</p>
                <div className='form_inputs'>
                    <div className='contact_inputs'>
                        <div className='contact_from_input'>
                            <input type='text' autoComplete='off' required='required'/>
                            <span>First Name</span>
                        </div>
                        <div className='contact_from_input'>
                            <input type='text' autoComplete='off' required='required'/>
                            <span>Email</span>
                        </div>
                    </div>
                    <div className='contact_inputs'>
                        <div className='contact_from_input'>
                            <input type='text' autoComplete='off' required='required'/>
                            <span>Last Name</span>
                        </div>
                        <div className='contact_from_input'>
                            <input type='text' autoComplete='off' required='required'/>
                            <span>Phone Number</span>
                        </div>
                    </div>
                </div>
                <div className='contact_subject'>
                <div className='contact_from_input'>
                            <input type='text' autoComplete='off' required='required'/>
                            <span>Subject</span>
                        </div>
                        </div>
                    <div className='contact_passage'>
                        <div className='contact_from_input'>
                            <textarea required='required'></textarea>
                            <span>Tell Us Something.....</span>
                        </div>
                    </div>
                    <div className='contact_button'>
                            <button>Send To Enigma</button>
                    </div>
            </div>
        </div>
    )
};
export default Contact_form;