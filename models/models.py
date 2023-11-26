from sqlalchemy import Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase
from sqlalchemy.ext.declarative import declared_attr
from datetime import datetime
from typing import Optional

class Base(DeclarativeBase):
    pass

class BaseModel:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


class Base(DeclarativeBase):
    pass

class User(Base, BaseModel):
    __tablename__ = 'user'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username:Mapped[str] = mapped_column(String(200), unique=True)
    password:Mapped[str] = mapped_column(String(255))


class ClientProfile(Base, BaseModel):
    __tablename__ = 'client_profile'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updated_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    created_by: Mapped[str] = mapped_column(String(200), ForeignKey("user.username", onupdate="CASCADE", ondelete="CASCADE"))
    updated_by: Mapped[str] = mapped_column(String(200), ForeignKey("user.username", onupdate="CASCADE", ondelete="CASCADE"))
    unique_id:Mapped[str] = mapped_column(String(100), unique=True)
    first_name:Mapped[str] = mapped_column(String(100))
    middle_name:Mapped[Optional[str]] = mapped_column(String(100))
    last_name:Mapped[str] = mapped_column(String(100))
    date_of_birth:Mapped[datetime] = mapped_column(DateTime)
    country_of_birth:Mapped[str] = mapped_column(String(100))
    gender:Mapped[str] = mapped_column(String(100))
    marital_status:Mapped[str] = mapped_column(String(100))
    occupation:Mapped[str] = mapped_column(String(100))
    gender_identity:Mapped[str] = mapped_column(String(100))
    sexual_orientation:Mapped[str] = mapped_column(String(100))
    phone_number:Mapped[Optional[str]] = mapped_column(String(100))
    address:Mapped[Optional[str]] = mapped_column(String(100))
    city:Mapped[Optional[str]] = mapped_column(String(100))
    state:Mapped[Optional[str]] = mapped_column(String(100))
    zip_code:Mapped[Optional[str]] = mapped_column(String(100))
    country:Mapped[Optional[str]] = mapped_column(String(100))
    email:Mapped[Optional[str]] = mapped_column(String(100))
    ethnicity:Mapped[Optional[str]] = mapped_column(String(100))
    race:Mapped[Optional[str]] = mapped_column(String(100))


class ClientScreening(BaseModel, Base):
    __tablename__ = "client_screening_sti"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
    created_by: Mapped[str] = mapped_column(String(200), ForeignKey("user.username", onupdate="CASCADE", ondelete="CASCADE"))
    updated_by: Mapped[str] = mapped_column(String(200), ForeignKey("user.username", onupdate="CASCADE", ondelete="CASCADE"))
    unique_id: Mapped[str] = mapped_column(String(64), ForeignKey("client_profile.unique_id", onupdate="CASCADE", ondelete="CASCADE"))
    date_of_screening: Mapped[Optional[datetime]] = mapped_column(DateTime)
    health_care_provider: Mapped[Optional[str]] = mapped_column(String(64))
    reporter_name: Mapped[Optional[str]]= mapped_column(String(64))
    reporter_contact: Mapped[Optional[str]] = mapped_column(String(64))
    sexual_partner_gender: Mapped[Optional[str]] = mapped_column(String(64))
    sexual_partner_gender_identity: Mapped[Optional[str]] = mapped_column(String(64))
    previous_HIV_screening: Mapped[Optional[str]] = mapped_column(String(10))
    previous_HIV_screening_date: Mapped[Optional[str]] = mapped_column(DateTime)
    previous_HIV_screening_result: Mapped[Optional[str]] = mapped_column(String(64))
    reason_for_testing: Mapped[Optional[str]] = mapped_column(String(64))
    screening_type: Mapped[Optional[str]] = mapped_column(String(64))
    site_of_sample_collection: Mapped[Optional[str]] = mapped_column(String(64))
    sample_collection_date: Mapped[Optional[datetime]] = mapped_column(DateTime)
    screening_result: Mapped[Optional[str]] = mapped_column(String(255))
    screening_notes: Mapped[Optional[str]] = mapped_column(String(255))
    diagnosis: Mapped[Optional[str]] = mapped_column(String(64))


class ClientTreatment(BaseModel, Base):
    __tablename__ = "client_treatment_sti"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
    created_by: Mapped[str] = mapped_column(String(200), ForeignKey("user.username", onupdate="CASCADE", ondelete="CASCADE"))
    updated_by: Mapped[str] = mapped_column(String(200), ForeignKey("user.username", onupdate="CASCADE", ondelete="CASCADE"))
    unique_id: Mapped[str] = mapped_column(String(64), ForeignKey("client_profile.unique_id", onupdate="CASCADE", ondelete="CASCADE"))
    date_of_treatment: Mapped[Optional[datetime]] = mapped_column(DateTime)
    health_care_provider: Mapped[Optional[str]] = mapped_column(String(64))
    reporter_name: Mapped[Optional[str]] = mapped_column(String(64))
    reporter_contact: Mapped[Optional[str]] = mapped_column(String(64))
    treatment_type: Mapped[Optional[str]] = mapped_column(String(64))
    treatment_plan: Mapped[Optional[str]] = mapped_column(String(64))
    treatment_notes: Mapped[Optional[str]] = mapped_column(String(64))
    treatment_result: Mapped[Optional[str]] = mapped_column(String(64))

class PartnerManagement(BaseModel, Base):
    __tablename__ = "partner_management_sti"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
    created_by: Mapped[str] = mapped_column(String(200), ForeignKey("user.username", onupdate="CASCADE", ondelete="CASCADE"))
    updated_by: Mapped[str] = mapped_column(String(200), ForeignKey("user.username", onupdate="CASCADE", ondelete="CASCADE"))
    unique_id: Mapped[str] = mapped_column(String(64),unique=True)
    partner_unique_id: Mapped[Optional[str]] = mapped_column(String(64), ForeignKey("client_profile.unique_id", onupdate="CASCADE", ondelete="CASCADE"))
    date_of_partner_management: Mapped[Optional[datetime]] = mapped_column(DateTime)
    health_care_provider: Mapped[Optional[str]] = mapped_column(String(64))
    reporter_name: Mapped[Optional[str]] = mapped_column(String(64))
    reporter_contact: Mapped[Optional[str]] = mapped_column(String(64))
    partner_management_type: Mapped[Optional[str]] = mapped_column(String(64))
    partner_management_plan: Mapped[Optional[str]] = mapped_column(String(64))
    partner_management_notes: Mapped[Optional[str]] = mapped_column(String(64))
    partner_management_result: Mapped[Optional[str]] = mapped_column(String(64))

class CongenitalSyphilis(BaseModel, Base):
    __tablename__ = "congenital_syphilis_mothers"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now())
    created_by: Mapped[str] = mapped_column(String(200), ForeignKey("user.username", onupdate="CASCADE", ondelete="CASCADE"))
    updated_by: Mapped[str] = mapped_column(String(200), ForeignKey("user.username", onupdate="CASCADE", ondelete="CASCADE"))
    date_of_report: Mapped[Optional[datetime]]= mapped_column(DateTime)
    unique_id: Mapped[Optional[str]] = mapped_column(String(64), ForeignKey("client_profile.unique_id", onupdate="CASCADE", ondelete="CASCADE"))
    test_at_first_visit: Mapped[Optional[str]] = mapped_column(String(64))
    test_at_28_32: Mapped[Optional[str]] = mapped_column(String(64))
    test_at_delivery: Mapped[Optional[str]] = mapped_column(String(64))
    date_of_test_1: Mapped[Optional[datetime]] = mapped_column(DateTime)
    type_of_test_1: Mapped[Optional[str]] = mapped_column(String(64))
    result_of_test_1: Mapped[Optional[str]] = mapped_column(String(64))
    titre_of_test_1: Mapped[Optional[str]] = mapped_column(String(64))
    date_of_test_2: Mapped[Optional[datetime]] = mapped_column(DateTime)
    type_of_test_2: Mapped[Optional[str]] = mapped_column(String(64))
    result_of_test_2: Mapped[Optional[str]] = mapped_column(String(64))
    titre_of_test_2: Mapped[Optional[str]] = mapped_column(String(64))
    date_of_test_3: Mapped[Optional[datetime]] = mapped_column(DateTime)
    type_of_test_3: Mapped[Optional[str]] = mapped_column(String(64))
    result_of_test_3: Mapped[Optional[str]] = mapped_column(String(64))
    titre_of_test_3: Mapped[Optional[str]] = mapped_column(String(64))
    hiv_status: Mapped[Optional[str]] = mapped_column(String(64))
    clinical_stage: Mapped[Optional[str]] = mapped_column(String(64))
    first_treatment: Mapped[Optional[str]] = mapped_column(String(64))
    trimester_of_first_treatment: Mapped[Optional[str]] = mapped_column(String(64))
    treatment_dose: Mapped[Optional[str]] = mapped_column(String(64))
    treatment_outcome: Mapped[Optional[str]] = mapped_column(String(64))
    treatment_response: Mapped[Optional[str]] = mapped_column(String(64))
    infant_unique_id: Mapped[Optional[str]] = mapped_column(String(64),unique=True)
    infant_first_name: Mapped[Optional[str]] = mapped_column(String(64))
    infant_middle_name: Mapped[Optional[str]] = mapped_column(String(64))
    infant_last_name: Mapped[Optional[str]] = mapped_column(String(64))


class CongenitalSyphilisInfant(BaseModel, Base):
    __tablename__ = "congenital_syphilis_infant"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    created_by: Mapped[str] = mapped_column(String(200), ForeignKey("user.username", onupdate="CASCADE", ondelete="CASCADE"))
    updated_by: Mapped[str] = mapped_column(String(200), ForeignKey("user.username", onupdate="CASCADE", ondelete="CASCADE"))
    infant_unique_id: Mapped[str] = mapped_column(String(64),ForeignKey("congenital_syphilis_mothers.infant_unique_id", onupdate="CASCADE", ondelete="CASCADE"))
    lmp_before_delivery: Mapped[Optional[datetime]] = mapped_column(DateTime)
    date_of_delivery: Mapped[Optional[datetime]] = mapped_column(DateTime)
    gestational_age_at_delivery: Mapped[Optional[str]] = mapped_column(String(64))
    birth_weight: Mapped[Optional[str]] = mapped_column(String(64))
    vital_status: Mapped[Optional[str]] = mapped_column(String(64))
    date_of_death: Mapped[Optional[datetime]] = mapped_column(DateTime)
    gestational_age_at_death: Mapped[Optional[str]] = mapped_column(String(64))
    date_of_first_test: Mapped[Optional[datetime]] = mapped_column(DateTime)
    type_of_first_test: Mapped[Optional[str]] = mapped_column(String(64))
    result_of_first_test: Mapped[Optional[str]] = mapped_column(String(64))
    titre_of_first_test: Mapped[Optional[str]]= mapped_column(String(64))
    date_of_second_test: Mapped[Optional[datetime]] = mapped_column(DateTime)
    type_of_second_test: Mapped[Optional[str]] = mapped_column(String(64))
    result_of_second_test: Mapped[Optional[str]] = mapped_column(String(64))
    titre_of_second_test: Mapped[Optional[str]] = mapped_column(String(64))
    dfa_special_stains: Mapped[Optional[str]] = mapped_column(String(64))
    signs_of_congenital_syphilis: Mapped[Optional[str]] = mapped_column(String(255))
    long_bone_xray: Mapped[Optional[str]] = mapped_column(String(64))
    CSF_VDRL: Mapped[Optional[str]] = mapped_column(String(64))
    CSF_WBC_CSF_protein: Mapped[Optional[str]]= mapped_column(String(64))
    treatment: Mapped[Optional[str]] = mapped_column(String(255))
    congenital_syphilis_classification: Mapped[Optional[str]] = mapped_column(String(64))



class HepatitisB(BaseModel, Base):
    __tablename__ = "hepatitis_b_mothers"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())
    created_by: Mapped[str] = mapped_column(String(200), ForeignKey("user.username", onupdate="CASCADE", ondelete="CASCADE"))
    updated_by: Mapped[str] = mapped_column(String(200), ForeignKey("user.username", onupdate="CASCADE", ondelete="CASCADE"))
    date_of_report: Mapped[Optional[datetime]] = mapped_column(DateTime)
    unique_id: Mapped[str] = mapped_column(String(64), ForeignKey("client_profile.unique_id", onupdate="CASCADE", ondelete="CASCADE"))
    estimated_date_of_delivery: Mapped[Optional[datetime]] = mapped_column(DateTime)
    HBsAg_result: Mapped[Optional[str]] = mapped_column(String(64))
    IgM_anti_HBC: Mapped[Optional[str]] = mapped_column(String(64))
    HBV_DNA: Mapped[Optional[str]] = mapped_column(String(64))
    HBeAg: Mapped[Optional[str]] = mapped_column(String(64))
    ob_provider: Mapped[Optional[str]] = mapped_column(String(255))
    ob_provider_contact: Mapped[Optional[str]] = mapped_column(String(64))
    ob_provider_address: Mapped[Optional[str]] = mapped_column(String(255))
    ob_provider_email: Mapped[Optional[str]] = mapped_column(String(64))
    expected_delivery_facility: Mapped[Optional[str]] = mapped_column(String(255))
    expected_delivery_facility_contact: Mapped[Optional[str]] = mapped_column(String(64))
    expected_delivery_facility_address: Mapped[Optional[str]] = mapped_column(String(255))
    type_of_insurance: Mapped[Optional[str]] = mapped_column(String(64))







