import { Component } from '@angular/core';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent {

  constructor(private authService: AuthService ) {}

  user: any = {}

  ngOnInit(): void {
    this.authService.getUser().subscribe((res: any) => {
      this.user = res;
    })
  }
}
