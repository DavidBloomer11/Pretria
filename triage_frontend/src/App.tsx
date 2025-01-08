import Header from "./components/Header";
import Footer from "./components/Footer";
import SymptomDescription from "./components/SymtpomDescription";
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container } from 'react-bootstrap';
import StartEncounter from "./components/StartEncounter";
import Triage from "./components/Triage";
import ForPatientsSection from "./components/ForPatientsSection";
import ForDoctorsSection from "./components/ForDoctorsSection";


function App() {
  return (
    <>
      <Header/>

      <div className="wrapper">
      <Container>

      <StartEncounter/>


      </Container>
      </div>

      <Footer/>
      

    </>
  );
}

export default App;