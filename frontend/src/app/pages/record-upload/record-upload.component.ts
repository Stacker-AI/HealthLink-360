import { Component } from '@angular/core';
import { FormBuilder, Validators, FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatStepperModule } from '@angular/material/stepper';
import { MatButtonModule } from '@angular/material/button';


@Component({
  selector: 'app-record-upload',
  templateUrl: './record-upload.component.html',
  styleUrls: ['./record-upload.component.css']
})
export class RecordUploadComponent {
  favoriteSeason!: string;
  bloods: string[] = ['Normal', 'High (Hypertension)', 'Low (Hypotension)', 'Not Sure'];

  hearts: string[] = ['Normal (60-100 bpm)', 'Tachycardia (High - Above 100 bpm)', 'Bradycardia (Low - Below 60 bpm)', 'Not Sure'];

  respiratories: string[] = ['Normal (12-20 breaths per minute)', 'Tachypnea (High - Above 20 breaths per minute)', 'Bradypnea (Low - Below 12 breaths per minute)', ' Not Sure'];

  tempes: string[] = ['Normal (98.6°F / 37°C)', 'Fever (Above 100.4°F / 38°C)', ' Hypothermia (Below 95°F / 35°C)', 'Not Sure '];

  heights: string[] = ['Below 150 cm', '150 - 170 cm', 'Above 170 cm', 'Not know'];

  weights: string[] = ['Underweight', 'Normal', ' Overweight', 'Not Sure'];

  bmis: string[] = ['Below 18.5 (Underweight)', '18.5 - 24.9 (Normal)', '25 - 29.9 (Overweight)', 'Above 30 (Obese)', 'Not Sure'];

  physicals: string[] = ['Sedentary (1 - Little to no exercise or physical activity)',
    'Light Activity (2 - Light exercise or activity such as walking, yoga)',
    'Moderate Activity (3 - Moderate exercise or activity such as cycling, swimming)',
    'Vigorous Activity (4 - Intense exercise or activity such as running, weightlifting)'];

  dietries: string[] = ['Balanced Diet', 'Vegetarian', 'Vegan', 'Other'];

  smokies: string[] = ['Non-Smoker', 'Former Smoker', 'Current Smoker'];

  alcohols: string[] = ['Non-Drinker', 'Occasional Drinker', 'Regular Drinker'];

  ills: string[] = ['None',
    'Flu',
    'Common Cold',
    'Asthma',
    'Diabetes',
    'Hypertension',
    'Other'
  ];

  chronics: string[] = ['None',
    ' Diabetes',
    'Hypertension',
    'Arthritis',
    'Heart Disease',
    'Respiratory Disorders',
    'Other'];

  surgeries: string[] = ['None',
    'Appendectomy',
    'Knee Surgery',
    'Cataract Surgery',
    'Heart Surgery',
    'Other'];

  allergies: string[] = ['None',
    'Pollen',
    'Dust',
    'Food Allergies',
    ' Medication Allergies',
    'Other'];

  histories: string[] = ['No known family history of diseases',
    'Diabetes',
    'Heart Disease',
    'Cancer',
    'High Blood Pressure',
    'Other'];

  currents: string[] = [
    'None',
    'Aspirin',
    'Paracetamol (Acetaminophen)',
    'Ibuprofen',
    'Antibiotics',
    'Other',
    'Dosages'];

  frequencies: string[] = ['Once a day',
    'Twice a day',
    'Three times a day',
    'Four times a day',
    'Other'];

  vaccines: string[] = ['None',
    'Influenza (Flu)',
    'Measles, Mumps, Rubella (MMR)',
    'Tetanus, Diphtheria, Pertussis (Tdap)',
    'Hepatitis B',
    'Varicella (Chickenpox)',
    'Human Papillomavirus (HPV)',
    'COVID-19',
    'Other'
  ];

  mentals: string[] = ['Low',
    'Moderate',
    'High'];

  sleeps: string[] = ['Regular', 'Irregular'];

  glucoses: string[] = ['Normal (70-100 mg/dL fasting)',
    ' High (Above 126 mg/dL fasting)',
    'Low (Below 70 mg/dL fasting)',
    'Not Sure'];

  choles: string[] = [
    'Desirable (Below 200 mg/dL)',
    'Borderline High (200-239 mg/dL)',
    'High (Above 240 mg/dL)',
    'Not Sure'];



  exercises: string[] = ['Cardiovascular (e.g., Running, Cycling)',
    'Strength Training (e.g., Weightlifting)',
    'Flexibility and Stretching (e.g., Yoga, Pilates)',
    'Combination (Multiple types)',
    'Other'];

  intensities: string[] = ['Daily - Moderate intensity',
    'Several times a week - High intensity',
    'Weekly - Varied intensity',
    'Irregular or Occasional',
    'Other'];

  cbcs: string[] = ['Normal',
    'Abnormal',
    'Not Sure'];

  mens: string[] = ['Regular (28-35 days cycle)',
    'Irregular (Varied cycle lengths)',
    'Painful periods (Dysmenorrhea)',
    'Heavy bleeding (Menorrhagia)',
    'Other'];

  pregnancies: string[] = ['No pregnancies',
    'Successful Pregnancies',
    'Complications',
    'Other'];

  hazards: string[] = ['None',
    'Chemical Exposure',
    'Physical Hazards (e.g., Noise, Radiation)',
    'Biological Hazards (e.g., Infectious Agents)',
    'Other'];

  alergies: string[] = ['None',
    'Pollen',
    'Dust',
    'Pet Dander',
    'Mold',
    'Other'];

  cares: string[] = [
    'Limited',
    'Adequate'];

  economies: string[] = ['Low',
    'Middle',
    'High',
  ];


  firstFormGroup = this._formBuilder.group({
    firstCtrl: ['', Validators.required],
  });
  secondFormGroup = this._formBuilder.group({
    secondCtrl: ['', Validators.required],
  });

  thirdFormGroup = this._formBuilder.group({
    thirdCtrl: ['', Validators.required],
  });

  fourthFormGroup = this._formBuilder.group({
    fourthCtrl: ['', Validators.required],
  });

  fifthFormGroup = this._formBuilder.group({
    fifthCtrl: ['', Validators.required],
  });

  sixthFormGroup = this._formBuilder.group({
    sixthCtrl: ['', Validators.required],
  });

  seventhFormGroup = this._formBuilder.group({
    seventhCtrl: ['', Validators.required],
  });

  eighthFormGroup = this._formBuilder.group({
    eighthCtrl: ['', Validators.required],
  });

  ninthFormGroup = this._formBuilder.group({
    ninthCtrl: ['', Validators.required],
  });

  tenthFormGroup = this._formBuilder.group({
    ninthCtrl: ['', Validators.required],
  });

  eleventhFormGroup = this._formBuilder.group({
    eleventhCtrl: ['', Validators.required],
  });

  twelvethFormGroup = this._formBuilder.group({
    twelvethCtrl: ['', Validators.required],
  });
  isLinear = false;

  constructor(private _formBuilder: FormBuilder) { }
}
