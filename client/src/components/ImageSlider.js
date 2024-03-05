import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';
import Slider from 'react-slick';
import './ImageSlider.css';
const ImgSlider = (props)=>{
    let settings = {
        dots: true,
        infinite: true,
        speed: 200,
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
    };
    return (
        <div>
        <Slider {...settings}>
            <div className='wrap'>
               <img src='/images/Vectorslider1.png' alt=''/>
            </div>
            <div className='wrap'>
                <img src='/images/Vectorslider_2.png' alt=''/>
            </div>
            <div className='wrap'>
                <img src='/images/Vectorslider_3.png' alt=''/>
            </div>
        </Slider>
        </div>
    )
}
export default ImgSlider;