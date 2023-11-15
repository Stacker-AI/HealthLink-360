import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http: HttpClient) { }

  accessToken = "";

  register(body: any) {
    return this.http.post(' http://127.0.0.1:8000/api/register', body)
  }

  login(body: any) {
    return this.http.post(' http://127.0.0.1:8000/api/login', body, { withCredentials: true })
  }
}

