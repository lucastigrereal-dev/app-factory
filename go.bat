@echo off
echo ==========================================
echo APP FACTORY v3.1 — Forja Enterprise E2E
echo ==========================================
cd /d "C:\Users\lucas\Desktop\O_OMNISVERSO_REAL\SystemOS antiga pp factory"

echo.
echo [1/4] Smoke Tests v1 + v2...
python tests\smoke_test.py
if errorlevel 1 goto :erro
python tests\smoke_test_v2.py
if errorlevel 1 goto :erro

echo.
echo [2/4] Gerando app demo (Dashboard)...
python src\orchestrator_v2.py --idea "Dashboard de vendas para ecommerce" --app-name "demo-vendas" --type dashboard

echo.
echo [3/4] Abrindo frontend no browser...
start artifacts\demo-vendas\frontend\index.html

echo.
echo [4/4] Status dos apps gerados:
dir /b artifacts\

echo.
echo ==========================================
echo DONE — 3 tipos de app prontos:
echo   dashboard, saas, crm
echo   Comando: python src/orchestrator_v2.py --idea "..." --app-name "..."
echo ==========================================
goto :fim

:erro
echo [ERRO] Smoke test falhou. Verifique Ollama na porta 11434.

:fim
pause
