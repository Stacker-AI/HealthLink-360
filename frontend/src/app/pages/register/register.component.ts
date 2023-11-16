import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder } from '@angular/forms'
import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  form!: FormGroup;

  constructor(private formBuilder: FormBuilder, private http: HttpClient, private router: Router, private authService: AuthService) { }

  ngOnInit(): void {
    this.form = this.formBuilder.group({
      username: '',
      email: '',
      password1: '',
      password2: ''
    });
  }

  submit() {
    this.authService.register(this.form.getRawValue()).subscribe(() => {
      this.router.navigate(['/login'])
    })

  }
}