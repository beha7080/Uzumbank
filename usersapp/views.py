# # from .models import UzumUser
# from rest_framework.views import APIView
# from .serializers import UpdatePasswordSerializer, NewSerializer
# from rest_framework.response import Response
# from rest_framework import status
# #
# #
# # class BarchaUser(APIView):
# #     # GET: Barcha foydalanuvchilarni olish
# #     def get(self, request, id):
# #         odamlar = UzumUser.objects.all().filter(id=id)  # Barcha foydalanuvchilarni olib keladi
# #         serializer = UzumUserSerializer(odamlar, many=True)  # Seriyalashtiradi
# #         return Response(serializer.data)
# #
# #
# #
# #
# #     # POST: Yangi foydalanuvchi yaratish
# #     # def post(self, request):
# #     #     serializer = UzumUserSerializer(data=request.data)  # Yangi foydalanuvchi ma'lumotlarini seriyalashtiradi
# #     #     if serializer.is_valid():  # Validatsiya qiladi
# #     #         serializer.save()  # Saqlaydi
# #     #         return Response(serializer.data, status=status.HTTP_201_CREATED)  # Muvaffaqiyatli javob qaytaradi
# #     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Xatolikni qaytaradi
# #
# #     # # PUT: Foydalanuvchini to‘liq o‘zgartirish
# #     # def put(self, request, pk):
# #     #     try:
# #     #         user = UzumUser.objects.get(pk=pk)  # ID bo‘yicha foydalanuvchini topadi
# #     #     except UzumUser.DoesNotExist:
# #     #         return Response({"error": "Foydalanuvchi topilmadi"}, status=status.HTTP_404_NOT_FOUND)  # Topilmasa, xatolik qaytaradi
# #     #
# #     #     serializer = UzumUserSerializer(user, data=request.data)  # Seriyalashtiradi
# #     #     if serializer.is_valid():
# #     #         serializer.save()  # O‘zgarishlarni saqlaydi
# #     #         return Response(serializer.data)
# #     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Xato bo‘lsa, xatolikni qaytaradi
# #     #
# #     # # PATCH: Foydalanuvchini qisman o‘zgartirish
# #     # def patch(self, request, pk):
# #     #     try:
# #     #         user = UzumUser.objects.get(pk=pk)  # ID bo‘yicha foydalanuvchini topadi
# #     #     except UzumUser.DoesNotExist:
# #     #         return Response({"error": "Foydalanuvchi topilmadi"}, status=status.HTTP_404_NOT_FOUND)
# #     #
# #     #     serializer = UzumUserSerializer(user, data=request.data, partial=True)  # Faqat o‘zgartirilayotgan qismni seriyalashtiradi
# #     #     if serializer.is_valid():
# #     #         serializer.save()
# #     #         return Response(serializer.data)
# #     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# #     #
# #     # # DELETE: Foydalanuvchini o‘chirish
# #     # def delete(self, request, pk):
# #     #     try:
# #     #         user = UzumUser.objects.get(pk=pk)  # ID bo‘yicha foydalanuvchini topadi
# #     #     except UzumUser.DoesNotExist:
# #     #         return Response({"error": "Foydalanuvchi topilmadi"}, status=status.HTTP_404_NOT_FOUND)
# #     #
# #     #     user.delete()  # Foydalanuvchini o‘chiradi
# #     #     return Response({"message": "Foydalanuvchi muvaffaqiyatli o‘chirildi"}, status=status.HTTP_204_NO_CONTENT)
#
#
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import User
# from .serializers import UpdatePasswordSerializer
#
# class RegisterView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class LoginView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = User.objects.filter(username=username, password=password).first()
#         if user:
#             serializer = UserSerializer(user)
#             return Response({"message": "Login successful", "user": serializer.data}, status=200)
#         return Response({"detail": "Invalid credentials"}, status=401)
#
#
# class AllUsersView(APIView):
#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# class UserDetailView(APIView):
#     def get(self, request, id):
#         user = User.objects.all().filter(id=id).first()
#         serializer = UserSerializer(user)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# class UpdatePasswordUser(APIView):
#     serializer_class = UpdatePasswordSerializer
#
#     def put(self, request):
#         username = request.data.get('username')
#         old_password = request.data.get('old_password')
#         new_password = request.data.get('new_password')
#         new_last_name = request.data.get('new_last_name')  # Last name yangilash uchun
#
#         user = User.objects.filter(username=username, password=old_password).first()
#
#         if user:
#             user.password = new_password
#             if new_last_name:  # Agar new_last_name berilgan bo‘lsa, uni ham yangilaymiz
#                 user.last_name = new_last_name
#             user.save()
#             return Response({"message": "Password and last name updated successfully"}, status=status.HTTP_200_OK)
#
#         return Response({"detail": "User not found or Password Incorrect"}, status=status.HTTP_400_BAD_REQUEST)
#
# class UpdateData(APIView):
#     serializer_class = NewSerializer
#
#     def patch(self, request):
#         username = request.data.get('username')
#         old_password = request.data.get('old_password')
#         new_password = request.data.get('new_password')
#         new_username = request.data.get('new_username')
#         if User.objects.all().filter(username=username, password=old_password).exists():
#             User.objects.filter(username=username).update(password=new_password, username=new_username)
#             return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)
#         else:
#             return Response({"detail": "User not found or Password Incorrect"}, status=status.HTTP_400_BAD_REQUEST)
#
# class UpdateLastName(APIView):
#     serializer_class = UpdatePasswordSerializer
#
#     def patch(self, request):
#         username = request.data.get('username')
#         new_last_name = request.data.get('new_last_name')
#
#         user = User.objects.filter(username=username).first()
#         if user:
#             user.last_name = new_last_name
#             user.save()
#             return Response({"message": "Last name updated successfully"}, status=status.HTTP_200_OK)
#         return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)


# from .models import UzumUser
# from rest_framework.views import APIView
# from .serializers import UpdatePasswordSerializer, NewSerializer
# from rest_framework.response import Response
# from rest_framework import status
#
#
# class BarchaUser(APIView):
#     # GET: Barcha foydalanuvchilarni olish
#     def get(self, request, id):
#         odamlar = UzumUser.objects.all().filter(id=id)  # Barcha foydalanuvchilarni olib keladi
#         serializer = UzumUserSerializer(odamlar, many=True)  # Seriyalashtiradi
#         return Response(serializer.data)
#
#
#
#
#     # POST: Yangi foydalanuvchi yaratish
#     # def post(self, request):
#     #     serializer = UzumUserSerializer(data=request.data)  # Yangi foydalanuvchi ma'lumotlarini seriyalashtiradi
#     #     if serializer.is_valid():  # Validatsiya qiladi
#     #         serializer.save()  # Saqlaydi
#     #         return Response(serializer.data, status=status.HTTP_201_CREATED)  # Muvaffaqiyatli javob qaytaradi
#     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Xatolikni qaytaradi
#
#     # # PUT: Foydalanuvchini to‘liq o‘zgartirish
#     # def put(self, request, pk):
#     #     try:
#     #         user = UzumUser.objects.get(pk=pk)  # ID bo‘yicha foydalanuvchini topadi
#     #     except UzumUser.DoesNotExist:
#     #         return Response({"error": "Foydalanuvchi topilmadi"}, status=status.HTTP_404_NOT_FOUND)  # Topilmasa, xatolik qaytaradi
#     #
#     #     serializer = UzumUserSerializer(user, data=request.data)  # Seriyalashtiradi
#     #     if serializer.is_valid():
#     #         serializer.save()  # O‘zgarishlarni saqlaydi
#     #         return Response(serializer.data)
#     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Xato bo‘lsa, xatolikni qaytaradi
#     #
#     # # PATCH: Foydalanuvchini qisman o‘zgartirish
#     # def patch(self, request, pk):
#     #     try:
#     #         user = UzumUser.objects.get(pk=pk)  # ID bo‘yicha foydalanuvchini topadi
#     #     except UzumUser.DoesNotExist:
#     #         return Response({"error": "Foydalanuvchi topilmadi"}, status=status.HTTP_404_NOT_FOUND)
#     #
#     #     serializer = UzumUserSerializer(user, data=request.data, partial=True)  # Faqat o‘zgartirilayotgan qismni seriyalashtiradi
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(serializer.data)
#     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     #
#     # # DELETE: Foydalanuvchini o‘chirish
#     # def delete(self, request, pk):
#     #     try:
#     #         user = UzumUser.objects.get(pk=pk)  # ID bo‘yicha foydalanuvchini topadi
#     #     except UzumUser.DoesNotExist:
#     #         return Response({"error": "Foydalanuvchi topilmadi"}, status=status.HTTP_404_NOT_FOUND)
#     #
#     #     user.delete()  # Foydalanuvchini o‘chiradi
#     #     return Response({"message": "Foydalanuvchi muvaffaqiyatli o‘chirildi"}, status=status.HTTP_204_NO_CONTENT)
#
#
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.shortcuts import get_object_or_404
# from .models import User
# from .serializers import UserSerializer
#
#
# class RegisterView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class LoginView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = User.objects.filter(username=username, password=password).first()
#         if user:
#             serializer = UserSerializer(user)
#             return Response({"message": "Login successful", "user": serializer.data}, status=200)
#         return Response({"detail": "Invalid credentials"}, status=401)
#
#
# class AllUsersView(APIView):
#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# class UserDetailView(APIView):
#     def get(self, request, id):
#         user = User.objects.all().filter(id=id).first()
#         serializer = UserSerializer(user)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# class UpdatePasswordUser(APIView):
#     serializer_class = UpdatePasswordSerializer
#
#     def put(self, request):
#         username = request.data.get('username')
#         old_password = request.data.get('old_password')
#         new_password = request.data.get('new_password')
#         if User.objects.all().filter(username=username, password=old_password).exists():
#             User.objects.filter(username=username).update(password=new_password)
#             return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)
#         else:
#             return Response({"detail": "User not found or Password Incorrect"}, status=status.HTTP_400_BAD_REQUEST)


# class UpdateData(APIView):
#     serializer_class = NewSerializer
#
#     def patch(self, request):
#         username = request.data.get('username')
#         old_password = request.data.get('old_password')
#         new_password = request.data.get('new_password')
#         new_username = request.data.get('new_username')
#         if User.objects.all().filter(username=username, password=old_password).exists():
#             User.objects.filter(username=username).update(password=new_password, username=new_username)
#             return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)
#         else:
#             return Response({"detail": "User not found or Password Incorrect"}, status=status.HTTP_400_BAD_REQUEST)
#
# class Updatelastname(APIView):
#     serializer_class = NewSerializer
#
#     def patch(self, request):
#         username = request.data.get('username')
#         old_password = request.data.get('old_password')
#         new_password = request.data.get('new_password')
#         if User.objects.all().filter(username=username, password=old_password).exists():
#             User.objects.filter(username=username).update(password=new_password)
#             return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)
#         else:
#             return Response({"detail": "User not found or Password Incorrect"}, status=status.HTTP_400_BAD_REQUEST)


# class Updatelastname(APIView):
#      serializer_class = NewSerializer
#
#      def put(self, request):
#          username = request.data.get('username')
#          old_password = request.data.get('old_password')
#          new_password = request.data.get('new_password')
#          new_name = request.data.get('new_name')
#          if User.objects.all().filter(username=username, password=old_password).exists():
#              User.objects.filter(username=username).update(password=new_password)
#              User.objects.filter(username=username).update(name=new_name)
#              return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)
#          else:
#              return Response({"detail": "User not found or Password Incorrect"}, status=status.HTTP_400_BAD_REQUEST)
#
# class UpdatephonenumberUser(APIView):
#     serializer_class = NewSerializer
#
#     def put(self, request):
#         username = request.data.get('username')
#         old_password = request.data.get('old_password')
#         new_password = request.data.get('new_password')
#         new_name = request.data.get('new_name')
#         phone_number = request.data.get('phone_number')
#         if User.objects.all().filter(username=username, password=old_password).exists():
#                  User.objects.filter(username=username).update(password=new_password)
#                  User.objects.filter(username=username).update(name=new_name)
#                  User.objects.filter(username=username).update(phone_number=phone_number)
#                  return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)
#         else:
#             return Response({"detail": "User not found or Password Incorrect"}, status=status.HTTP_400_BAD_REQUEST)
#



from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

User = get_user_model()

class UpdatephonenumberUser(APIView):
    def put(self, request):
        username = request.data.get('username')
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        new_name = request.data.get('new_name')
        phone_number = request.data.get('phone_number')

        try:
            user = User.objects.get(username=username)
            if user.check_password(old_password):
                user.set_password(new_password)
                user.name = new_name
                user.phone_number = phone_number
                user.save()
                return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "Incorrect password"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)


class RegisterView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        phone_number = request.data.get("phone_number")

        if User.objects.filter(username=username).exists():
            return Response({"detail": "Username already taken"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(username=username, phone_number=phone_number)
        user.set_password(password)
        user.save()
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
            else:
                return Response({"detail": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)


class AllUsersView(APIView):
    def get(self, request):
        users = User.objects.all().values("id", "username", "phone_number")
        return Response(users, status=status.HTTP_200_OK)


class UserDetailView(APIView):
    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
            return Response({"id": user.id, "username": user.username, "phone_number": user.phone_number}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)


class PasswordUpdateRateThrottle(UserRateThrottle):
    rate = '5/hour'  # Limit password change attempts

@method_decorator(csrf_protect, name='dispatch')
class UpdatePasswordUser(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [PasswordUpdateRateThrottle]

    def put(self, request):
        username = request.data.get("username")
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        confirm_password = request.data.get("confirm_password")

        # Input validation
        if not all([username, old_password, new_password, confirm_password]):
            return Response(
                {"detail": "All fields are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check if passwords match
        if new_password != confirm_password:
            return Response(
                {"detail": "New passwords do not match"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Prevent reusing old password
        if old_password == new_password:
            return Response(
                {"detail": "New password must be different from old password"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = User.objects.get(username=username)

            # Verify the requesting user is the same as the target user
            if request.user != user:
                return Response(
                    {"detail": "You can only change your own password"},
                    status=status.HTTP_403_FORBIDDEN
                )

            if user.check_password(old_password):
                # Validate password strength
                try:
                    validate_password(new_password, user)
                except ValidationError as e:
                    return Response(
                        {"detail": list(e.messages)},
                        status=status.HTTP_400_BAD_REQUEST
                    )

                # Update password
                user.set_password(new_password)
                user.save()

                # Optional: Log the password change
                from django.contrib.auth.signals import user_logged_in
                user_logged_in.send(
                    sender=user.__class__,
                    request=request,
                    user=user
                )

                return Response(
                    {
                        "message": "Password updated successfully",
                        "note": "Please login again with your new password"
                    },
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"detail": "Incorrect password"},
                    status=status.HTTP_400_BAD_REQUEST
                )

        except User.DoesNotExist:
            return Response(
                {"detail": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )