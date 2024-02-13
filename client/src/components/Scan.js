import React, { useState, useEffect } from "react";
import './Scan.css'

const Scanner = () => {
  const [targetUrl, setTargetUrl] = useState("");
  const [data, setData] = useState({ 
    crawl_links: [], 
    information_disclouser: [], 
    security_headers: [],
    url_based_sql_injection: [],
    blind_error_based: [],
    sql_blind_time_based: [],
    path_traversal: []
  });
  const [loading, setLoading] = useState(false);
  const [scanning, setScanning] = useState(false);

  let debounceTimeout;

  const fetchData = async () => {
    try {
      setLoading(true);
      setScanning(true);

      const response = await fetch(`http://localhost:5000/scanner?url=${targetUrl}`);
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const result = await response.json();
      setData(result);
    } catch (error) {
      console.error("Fetch error:", error);
    } finally {
      setLoading(false);
      setScanning(false);
    }
  };

  const handleInputChange = (e) => {
    const inputValue = e.target.value;
    setTargetUrl(inputValue);
  
    clearTimeout(debounceTimeout);
  
    debounceTimeout = setTimeout(() => {
      fetchData();
    }, 30000); // Adjust the delay as needed
  };
  const handleScanClick = () => {
    if (!scanning) {
      fetchData();
    }
  };

  const handleDownloadClick = async () => {
    try {
      const response = await fetch(`http://localhost:5000/download-report?url=${targetUrl}`);
      if (!response.ok) {
        throw new Error(`Failed to download report`)
      }
      //Start downloading the report
      const blob = await response.blob();
      const url = window.URL.createObjectURL(new Blob([blob]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', 'report.pdf');
      document.body.appendChild(link);
      link.click();
      link.parentNode.removeChild(link);
    } catch (error) {
      console.error("Download error:", error);
    }
  };

  return (
    <div className="scan_container">
      <div className="input-box">
        <input
          className="scan-link"
          type="text"
          value={targetUrl}
          onChange={handleInputChange}
          autoComplete="off"
          required="required"
        />
        <span>Enter Website URL</span>
        <button onClick={handleScanClick} disabled={scanning}>Scan</button><br />
      </div>

      {loading && <div className="spinner">Scanning</div>}

      

      <ol style={{ "--length": 5 }} role="list">
      {data.crawl_links && data.crawl_links.length === 0 && (
        <li style={{ "--i": 5 }}>
        <span>*Enter the Website link and make sure you copypaste the link*</span>
        </li>
      )}

      {data.crawl_links && data.crawl_links.length > 0 && (
        <li style={{ "--i": 5 }}>
        <div className="crawl-links">
          <h1>Crawled Links</h1>
          <div className="crawl-links-container">
            <ul>
              {data.crawl_links.map((link, index) => (
                <li key={index}>
                  <a href={link} target="_blank" rel="noopener noreferrer">
                    {link}
                  </a>
                </li>
              ))}
            </ul>
          </div>
        </div>
        </li>
      )}
        {data.url_based_sql_injection && data.url_based_sql_injection.length > 0 && (
          <li style={{ "--i": 1 }}>
            <div className="Findings">
              <h2 className="vulnerability-detected">Url Based SQL Injection Detected</h2>
              <ul>
                {data.url_based_sql_injection.map((info, index) => (
                  <p key={index} style={{ color: 'red' }}>
                    {info}
                  </p>
                ))}
              </ul>
            </div>
          </li>
        )}
        {data.blind_error_based && data.blind_error_based.length > 0 && (
          <li style={{ "--i": 1 }}>
            <div className="Findings">
              <h2 className="vulnerability-detected">Blind Error Based SQL Injection Detected</h2>
              <ul>
                {data.blind_error_based.map((info, index) => (
                  <li key={index} style={{ color: 'red' }}>
                    {info}
                  </li>
                ))}
              </ul>
            </div>
          </li>
        )}
        {data.sql_blind_time_based && data.sql_blind_time_based.length > 0 && (
          <li style={{ "--i": 1 }}>
            <div className="Findings">
              <h2 className="vulnerability-detected">SQL Time Based SQL Injection Detected</h2>
              <ul>
                {data.sql_blind_time_based.map((info, index) => (
                  <li key={index} style={{ color: 'red' }}>
                    {info}
                  </li>
                ))}
              </ul>
            </div>
          </li>
        )}
        {data.path_traversal && data.path_traversal.length > 0 && (
          <li style={{ "--i": 2 }}>
            <div className="Findings">
              <h2 className="vulnerability-detected">Path Traversal Detected</h2>
              <ul>
                {data.path_traversal.map((info, index) => (
                  <li key={index} style={{ color: 'red' }}>
                    {info}
                  </li>
                ))}
              </ul>
            </div>
          </li>
        )}
        {data.security_headers && data.security_headers.length > 0 && (
          <li style={{ "--i": 1 }}>
            <div className="Findings">
              <h2 className="vulnerability-detected">Security Headers Detected</h2>
              <ul>
                {data.security_headers.map((info, index) => (
                  <li key={index} style={{ color: 'red' }}>
                    {info}
                  </li>
                ))}
              </ul>
            </div>
          </li>
        )}
         {data.information_disclouser && data.information_disclouser.length > 0 && (
          <li style={{ "--i": 1 }}>
          <div className="Findings">
            <h2 className="vulnerability-detected">Information Disclosure Detected</h2>
            <ul>
              {data.information_disclouser.map((info, index) => (
                <li key={index} style={{ color: 'red' }}>
                  {info}
                </li>
              ))}
            </ul>
          </div>
          </li>
        )}
        {data.crawl_links && data.crawl_links.length > 0 && (
          <li style={{ "--i": 5 }}>
          <div className="report-download">
          <button onClick={handleDownloadClick}>Download Report</button>
        </div>
        </li>
        )}
      </ol>
      
    </div>
  );
};

export default Scanner;
