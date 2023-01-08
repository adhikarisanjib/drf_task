from rest_framework import serializers

from student_app.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

    def validate_grade(self, value):
        if int(value) > 12:
            raise serializers.ValidationError(f"Grade value must be between 1 to 12.")
        return value

    def validate_age(self, value):
        if int(value) < 4 or int(value) > 25:
            raise serializers.ValidationError(f"Age must be between 4 and 25 years.")
        return value