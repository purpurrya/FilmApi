from rest_framework import serializers


class CustomPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def to_representation(self, value):
        if self.pk_field is not None:
            return self.pk_field.to_representation(value.pk)
        return {"id": value.pk}


class CustomChoiceField(serializers.ChoiceField):
    def to_representation(self, value):
        if value in ("", None):
            return value
        return self._choices[value]

    def to_internal_value(self, data):
        if data == "":
            raise serializers.ValidationError("This field is required")
        for key, value in self._choices.items():
            if value == data:
                return key
        self.fail("invalid_choice", input=data)
