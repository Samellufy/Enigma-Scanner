import React, { useState, useEffect } from "react";
import './Scan.css'
import { Link } from "react-router-dom";
import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';

const Scanner = () => {
  const [userId, setUserId] = useState("");
  const [isSubscribed, setIsSubscribed] = useState(false);

  useEffect(() => {
      const unsubscribe = firebase.auth().onAuthStateChanged(async (user) => {
          if (user) {
              setUserId(user.uid);
              checkSubscription(user.uid)
          } else {
              // User is signed out.
              // You can handle this case if needed.
          }
      });

      return () => {
          unsubscribe();
      };
  }, []);

  // const checkout = async () => {
  //     try {
  //         console.log(userId);
  //         // Create a new collection 'subscribedUsers' and add the user to it
  //         firebase.firestore().collection('subscribedUsers').add({
  //             userId: userId,
  //             // You can add more user information here if needed
  //         });

  //         console.log("User subscribed successfully!");
  //     } catch (error) {
  //         console.error("Error subscribing user:", error);
  //     }
  // };

  const checkSubscription = async (userId) => {
      try {
          const subscribedUsersRef = firebase.firestore().collection('subscribedUsers');
          const querySnapshot = await subscribedUsersRef.where('userId', '==', userId).get();
  
          if (!querySnapshot.empty && querySnapshot.docs.length > 0) {
              // User document exists in the collection, indicating subscription
              setIsSubscribed(true);
              console.log("user subscribed");
              
          } else {
              // User document does not exist in the collection, indicating no subscription
              setIsSubscribed(false);
              console.log("user not subscribed");
          }
      } catch (error) {
          console.error("Error checking subscription:", error);
          setIsSubscribed(false); // Set subscription status to false in case of an error
      }
  };
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
      setData({});

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
  const non_sub_fetchData = async () => {
    try {
      setLoading(true);
      setScanning(true);
      setData({});

      const response = await fetch(`http://localhost:5000/non_sub_scanner?url=${targetUrl}`);
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
    setTargetUrl(e.target.value);
  };

  const handleScanClick = () => {
    if (!scanning) {
      fetchData();
    }
  };  
  const handlenonsubScanClick = () => {
    if (!scanning) {
      non_sub_fetchData();
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
  // const handleDownloadClick = async () => {
  //   try {
  //     const response = await fetch(`http://localhost:5000/download-report?url=${targetUrl}`);
  //     if (!response.ok) {
  //       throw new Error(`Failed to download report`);
  //     }
  
  //     // Prompt user to select download location
  //     const downloadPath = window.prompt("Enter download path (including file name):");
  //     if (!downloadPath) return; // If user cancels, do nothing
  
  //     // Start downloading the report
  //     const blob = await response.blob();
  //     const url = window.URL.createObjectURL(new Blob([blob]));
  //     const link = document.createElement('a');
  //     link.href = url;
  
  //     // Set custom download path
  //     link.setAttribute('download', downloadPath);
      
  //     document.body.appendChild(link);
  //     link.click();
  //     link.parentNode.removeChild(link);
  //     await firebase.firestore().collection('downloadedReports').add({
  //       userId: userId,
  //       downloadPath: downloadPath,
  //       // You can add more information such as timestamp, etc., if needed
  //     });
  //   } catch (error) {
  //     console.error("Download error:", error);
  //   }
  // };
  const handlePreviousReportClick = async () => {
    try {
        // Fetch previous report path from Firestore
        const reportsRef = firebase.firestore().collection('downloadedReports');
        const querySnapshot = await reportsRef.where('userId', '==', userId).limit(1).get();
        if (!querySnapshot.empty) {
            const reportData = querySnapshot.docs[0].data();
            const previousReportPath = reportData.downloadPath;

            console.log("Previous report path:", previousReportPath); // Log the URL

            // Start downloading the previous report
            const response = await fetch(previousReportPath);
            if (!response.ok) {
                throw new Error(`Failed to download previous report`);
            }

            // Prompt user to select download location
            const downloadPath = window.prompt("Enter download path (including file name):");
            if (!downloadPath) return; // If user cancels, do nothing

            // Start downloading the report
            const blob = await response.blob();
            const url = window.URL.createObjectURL(new Blob([blob]));
            const link = document.createElement('a');
            link.href = url;

            // Set custom download path
            link.setAttribute('download', downloadPath);
            
            document.body.appendChild(link);
            link.click();
            link.parentNode.removeChild(link);
        } else {
            console.log("No previous report found for the user.");
        }
    } catch (error) {
        console.error("Previous report download error:", error);
    }
};


  return (
    <div className="scan_container">
      {isSubscribed ? (
        <React.Fragment>
                     <div className="input-box">
                     <input
                       className="scan-link"
                       type="text"
                       value={targetUrl}
                       onChange={handleInputChange}
                       autoComplete="off"
                       required="required"
                       disabled={scanning}
                     />
                     <span>Enter Website URL</span>
                     <button onClick={handleScanClick} disabled={scanning}>Scan</button><br />
                   </div>
             
                  {loading && <div className="spinner">Scanning</div>}
             
                   
             
                   <ol style={{ "--length": 5 }} role="list">
                   {data.crawl_links && data.crawl_links.length === 0 && (
                     <li style={{ "--i": 2 }}>
                     <span>*Enter the Website link and make sure you copypaste the link*</span>
                     </li>
                   )}
                   {data.not_200 && data.not_200.length > 0 &&(
                    <li style={{ "--i": 1 }}>
                    <div className="crawl-links">
                      <h1>Entered Link is not a valid link please check</h1>
                    </div>
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
                       <li style={{ "--i": 1 }}>
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
                   </React.Fragment>
      ):(
        <React.Fragment>
        <div className="input-box">
        <input
          className="scan-link"
          type="text"
          value={targetUrl}
          onChange={handleInputChange}
          autoComplete="off"
          required="required"
          disabled={scanning}
        />
        <span>Enter Website URL</span>
        <button onClick={handlenonsubScanClick} disabled={scanning}>Scan</button><br />
      </div>

     {loading && <div className="spinner">Scanning</div>}

      

      <ol style={{ "--length": 5 }} role="list">
      {data.crawl_links && data.crawl_links.length === 0 && (
        <li style={{ "--i": 2 }}>
        <span>*Enter the Website link and make sure you copypaste the link*</span>
        </li>
      )}

      {data.not_200 && data.not_200.length > 0 &&(
          <li style={{ "--i": 1 }}>
          <div className="crawl-links">
          <h1>Entered Link is not a valid link please check</h1>
          </div>
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
                     
            <div className="report-download">
                         <li style={{ "--i": 5 }}>
                          <p>Embark on a comprehensive vulnerability scan to unearth even the most elusive and critical security weaknesses, ensuring robust protection for your digital assets and invaluable peace of mind.</p>
                  <Link to='/subscribe'>
                    <button>Subscribe</button>
                    </Link>
                    </li>
              </div>
              </ol>
              </React.Fragment>
      )}
                
      </div>
    
  );
};

export default Scanner;
