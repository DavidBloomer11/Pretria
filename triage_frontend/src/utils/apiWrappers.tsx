import axios, { Axios } from "axios";

class EncounterApi {
  private uuid: string = "";
  private url: string;
  private csrf: string;
  private axios: Axios;

  constructor(uuid: string) {
    this.uuid = uuid;
    this.url = window.location.origin;
    this.csrf = this.getCookie("csrftoken");
    this.axios = axios;
    this.axios.defaults.headers.common['X-CSRFToken'] = this.csrf;
    
  }

  public get() {
    this.axios
      .get(`${this.url}/api/encounters/${this.uuid}`)
      .then(function (response) {});
  }

  // Creates an encounter object and returns the uuid
  public async create() {
    return await axios
      .post(`${this.url}/api/encounters/`)
      .then((response) => {
        return response;
      })
      .catch((error) => {
        console.log(error);
        throw error;
      });
  }

  public async update(data: any) {
    return await this.axios
      .patch(`${this.url}/api/encounters/${this.uuid}/`, data)
      .then((response) => {
        return response;
      })
      .catch((error) => {
        throw error;
      });
  }

  public async generateQuestions() {
    return await this.axios
      .post(`${this.url}/api/encounters/${this.uuid}/generate_questions/`)
      .then((response) => {
        return response;
      })
      .catch((error) => {
        throw error;
      });
  }

  public async updateAnswer(data: any, encounterQuestionId: number) {
    return await this.axios
      .patch(
        `${this.url}/api/encounters/${this.uuid}/questions/${encounterQuestionId}/`,
        data
      )
      .then((response) => {
        return response;
      })
      .catch((error) => {
        throw error;
      });
  }

  //Wrapper to generate triage prediction
  public async generateTriage() {
    return await this.axios
      .post(`${this.url}/api/encounters/${this.uuid}/generate_triage/`)
      .then((response) => {
        return response;
      })
      .catch((error) => {
        throw error;
      });
  }

  //Get cookie
  public getCookie(name: string) {
    // Split all cookies into an array
    const cookies = document.cookie.split(";");

    // Loop through all cookies
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();

      // Check if the cookie name matches
      if (cookie.startsWith(name + "=")) {
        // Extract the cookie value and return it
        return cookie.substring(name.length + 1, cookie.length);
      }
    }

    // Cookie not found
    return "";
  }
}

export default EncounterApi;
