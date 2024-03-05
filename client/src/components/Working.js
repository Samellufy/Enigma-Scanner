import './Working.css'
const Working = (props) => {
  return (
    <div className="working_content">
      <div className="inner_content">
        <h1>
          HOW DO ENIGMA <br />
          SCANS
        </h1>
        <img src="/icon/Component 1intro_arrow.png" alt="arrow" />
        <p>
          Enigma Scanner employs a multi-faceted approach to scanning that
          combines advanced techniques to comprehensively evaluate the security
          posture of web applications.
        </p>
      </div>
      <div className="working_no">
        <div className='working_steps'>
            <h1>01</h1>
        </div>
        <div className='working_steps'>
            <h1>02</h1>
        </div>
        <div className='working_steps'>
            <h1>03</h1>
        </div>
        <div className='working_steps'>
            <h1>04</h1>
        </div>
      </div>
      <div className='working_dstep'>
        <div className='working_dstep_inner'>
        <img src='/images/arrow-small-rightsmall_arr.png' alt='small arrow'/>
        <p>Take's Website URL</p>
        </div>
        <div className='working_dstep_inner'>
        <img src='/images/arrow-small-rightsmall_arr.png' alt='small arrow'/>
        <p>Crawl the Website</p>
        </div>
        <div className='working_dstep_inner'>
        <img src='/images/arrow-small-rightsmall_arr.png' alt='small arrow'/>
        <p>Scan for Vulnerabilities</p>
        </div>
        <div className='working_dstep_inner'>
        <img src='/images/arrow-small-rightsmall_arr.png' alt='small arrow'/>
        <p>Generate Report</p>
        </div>
      </div>
    </div>
  );
};
export default Working;
