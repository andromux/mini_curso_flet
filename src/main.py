#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import flet as ft
import httpx
import asyncio
from datetime import datetime
from urllib.parse import quote
import threading
import os

class GitHubNightlyApp:
    def __init__(self):
        self.artifacts_data = []
        self.current_run_id = None
        
    def get_headers(self, token):
        headers = {
            "Accept": "application/vnd.github+json",
        }
        if token:
            headers["Authorization"] = f"Bearer {token}"
        return headers

    def fetch_latest_run(self, owner, repo, workflow, headers):
        url = f"https://api.github.com/repos/{owner}/{repo}/actions/workflows/{workflow}/runs"
        params = {
            "status": "completed",
            "conclusion": "success",
            "per_page": 1
        }
        try:
            response = httpx.get(url, headers=headers, params=params, timeout=30.0)
            response.raise_for_status()
        except httpx.HTTPError as e:
            raise Exception(f"Error al obtener el run: {e}")

        runs = response.json().get("workflow_runs", [])
        if not runs:
            raise Exception("No se encontró un run exitoso para ese workflow.")

        return runs[0]["id"]

    def fetch_artifacts(self, owner, repo, run_id, headers):
        url = f"https://api.github.com/repos/{owner}/{repo}/actions/runs/{run_id}/artifacts"
        try:
            response = httpx.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
        except httpx.HTTPError as e:
            raise Exception(f"Error al obtener los artefactos: {e}")

        return response.json().get("artifacts", [])

    def save_output(self, filename, artifacts, owner, repo, run_id):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# Quick Nightly Links - {datetime.now()}\n")
            f.write(f"# Repository: {owner}/{repo}\n")
            f.write(f"# Run ID: {run_id}\n\n")
            for artifact in artifacts:
                name = artifact["name"]
                size = int(artifact["size_in_bytes"]) // 1024 // 1024
                safe_name = quote(name)
                link = f"https://nightly.link/{owner}/{repo}/actions/runs/{run_id}/{safe_name}.zip"
                f.write(f"# {name} ({size} MB)\n{link}\n\n")
            f.write(f"# Todos los artefactos:\nhttps://nightly.link/{owner}/{repo}/actions/runs/{run_id}\n")

    def process_artifacts(self, page, repo_field, workflow_field, token_field, status_text, artifacts_column, save_btn, all_artifacts_btn):
        try:
            # Validar entrada
            if '/' not in repo_field.value:
                status_text.value = "❌ El repositorio debe tener formato owner/repo"
                status_text.color = ft.Colors.RED
                page.update()
                return

            owner, repo = repo_field.value.split("/", 1)
            headers = self.get_headers(token_field.value)

            # Actualizar estado
            status_text.value = f"🔍 Buscando última ejecución exitosa en: {owner}/{repo}"
            status_text.color = ft.Colors.BLUE
            page.update()

            # Obtener run ID
            run_id = self.fetch_latest_run(owner, repo, workflow_field.value, headers)
            self.current_run_id = run_id
            
            status_text.value = f"✅ Último Run ID: {run_id}"
            status_text.color = ft.Colors.GREEN
            page.update()

            # Obtener artefactos
            status_text.value = "📦 Obteniendo artefactos..."
            page.update()
            
            artifacts = self.fetch_artifacts(owner, repo, run_id, headers)
            self.artifacts_data = artifacts
            
            if not artifacts:
                status_text.value = "⚠️ No hay artefactos para este run."
                status_text.color = ft.Colors.ORANGE
                page.update()
                return

            # Limpiar lista anterior
            artifacts_column.controls.clear()
            
            # Mostrar artefactos
            for artifact in artifacts:
                name = artifact["name"]
                size = int(artifact["size_in_bytes"]) // 1024 // 1024
                safe_name = quote(name)
                link = f"https://nightly.link/{owner}/{repo}/actions/runs/{run_id}/{safe_name}.zip"
                
                # Crear card para cada artefacto
                card = ft.Card(
                    content=ft.Container(
                        content=ft.Column([
                            ft.Text(name, weight=ft.FontWeight.BOLD, size=16),
                            ft.Text(f"Tamaño: {size} MB", size=12, color=ft.Colors.GREY_700),
                            ft.Row([
                                ft.ElevatedButton(
                                    "Copiar Link",
                                    icon=ft.Icons.COPY,
                                    on_click=lambda e, url=link: self.copy_to_clipboard(page, url)
                                ),
                                ft.ElevatedButton(
                                    "Abrir",
                                    icon=ft.Icons.OPEN_IN_NEW,
                                    on_click=lambda e, url=link: page.launch_url(url)
                                )
                            ])
                        ]),
                        padding=10
                    )
                )
                artifacts_column.controls.append(card)
            
            # Habilitar botones
            save_btn.disabled = False
            all_artifacts_btn.disabled = False
            all_artifacts_btn.data = f"https://nightly.link/{owner}/{repo}/actions/runs/{run_id}"
            
            status_text.value = f"✅ Encontrados {len(artifacts)} artefactos"
            status_text.color = ft.Colors.GREEN
            page.update()

        except Exception as e:
            status_text.value = f"❌ Error: {str(e)}"
            status_text.color = ft.Colors.RED
            page.update()

    def copy_to_clipboard(self, page, text):
        page.set_clipboard(text)
        page.show_snack_bar(ft.SnackBar(content=ft.Text("Link copiado al portapapeles!")))

    def save_file(self, page, repo_field):
        if not self.artifacts_data or not self.current_run_id:
            return
            
        try:
            owner, repo = repo_field.value.split("/", 1)
            filename = f"quick_links_{int(datetime.now().timestamp())}.txt"
            self.save_output(filename, self.artifacts_data, owner, repo, self.current_run_id)
            page.show_snack_bar(ft.SnackBar(content=ft.Text(f"Guardado en: {filename}")))
        except Exception as e:
            page.show_snack_bar(ft.SnackBar(content=ft.Text(f"Error al guardar: {str(e)}")))

def main(page: ft.Page):
    page.title = "GitHub Nightly Fetcher"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 800
    page.window_height = 600
    page.scroll = ft.ScrollMode.AUTO
    
    app = GitHubNightlyApp()
    
    # Componentes de la interfaz
    title = ft.Text(
        "🚀 GitHub Nightly Fetcher",
        size=24,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )
    
    repo_field = ft.TextField(
        label="Repositorio (owner/repo)",
        value="Sploder-Saptarshi/sm64coopdx-android",
        width=400,
        prefix_icon=ft.Icons.ACCOUNT_TREE
    )
    
    workflow_field = ft.TextField(
        label="Workflow YAML",
        value="build-coop.yaml",
        width=400,
        prefix_icon=ft.Icons.PLAY_ARROW
    )
    
    token_field = ft.TextField(
        label="Token GitHub (opcional)",
        password=True,
        can_reveal_password=True,
        width=400,
        prefix_icon=ft.Icons.KEY
    )
    
    status_text = ft.Text(
        "Listo para buscar artefactos",
        size=14,
        text_align=ft.TextAlign.CENTER
    )
    
    artifacts_column = ft.Column(
        spacing=10,
        scroll=ft.ScrollMode.AUTO
    )
    
    save_btn = ft.ElevatedButton(
        "💾 Guardar Links",
        icon=ft.Icons.SAVE,
        disabled=True,
        on_click=lambda e: app.save_file(page, repo_field)
    )
    
    all_artifacts_btn = ft.ElevatedButton(
        "🌍 Ver Todos los Artefactos",
        icon=ft.Icons.OPEN_IN_NEW,
        disabled=True,
        on_click=lambda e: page.launch_url(all_artifacts_btn.data) if all_artifacts_btn.data else None
    )
    
    fetch_btn = ft.ElevatedButton(
        "🔍 Buscar Artefactos",
        icon=ft.Icons.SEARCH,
        style=ft.ButtonStyle(
            color=ft.Colors.WHITE,
            bgcolor=ft.Colors.BLUE
        ),
        on_click=lambda e: threading.Thread(
            target=app.process_artifacts,
            args=(page, repo_field, workflow_field, token_field, status_text, artifacts_column, save_btn, all_artifacts_btn)
        ).start()
    )
    
    # Layout principal
    page.add(
        ft.Container(
            content=ft.Column([
                ft.Container(height=20),
                title,
                ft.Container(height=20),
                ft.Card(
                    content=ft.Container(
                        content=ft.Column([
                            ft.Text("Configuración", size=18, weight=ft.FontWeight.BOLD),
                            repo_field,
                            workflow_field,
                            token_field,
                            ft.Container(height=10),
                            fetch_btn
                        ]),
                        padding=20
                    )
                ),
                ft.Container(height=10),
                status_text,
                ft.Container(height=10),
                ft.Card(
                    content=ft.Container(
                        content=ft.Column([
                            ft.Text("Artefactos Disponibles", size=18, weight=ft.FontWeight.BOLD),
                            artifacts_column,
                            ft.Container(height=10),
                            ft.Row([
                                save_btn,
                                all_artifacts_btn
                            ])
                        ]),
                        padding=20
                    )
                )
            ]),
            padding=20
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
