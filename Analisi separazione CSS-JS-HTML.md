# Analisi separazione CSS / JS / HTML  
  
Verifica violazioni della separazione tra logica JS, HTML e CSS nella codebase.  
Esclusi i file `splash/project/SPLASH Wireframes*` (file di design/wireframe, non parte dell'app).  
  
Cartella analizzata: `src/main/webapp`  
  
## 1. Tag `<style>` embedded → spostare su CSS esterno  
  
| File | Occorrenze |  
|------|-----------|  
| `jsp/views/my-notifications-management.jsp` | 1 |  
| `jsp/views/send-notification-management.jsp` | 1 |  
| `jsp/views/notifications-management.jsp` | 1 |  
  
## 2. Stili inline (attributo `style=`) → spostare su CSS esterno  
  
| File | Occorrenze |  
|------|-----------|  
| `jsp/views/users-management.jsp` | 47 |  
| `jsp/views/roles-management.jsp` | 39 |  
| `jsp/views/my-notifications-management.jsp` | 6 |  
| `html/components/sidebar.html` | 5 |  
| `jsp/views/notifications-management.jsp` | 4 |  
| `html/send-notification.html` | 1 |  
| `jsp/views/send-notification-management.jsp` | 1 |  
  
## 3. Script embedded (`<script>` senza `src`) → spostare su JS esterno  
  
| File | Embedded |  
|------|----------|  
| `jsp/views/send-notification-management.jsp` | 1 |  
| `jsp/views/roles-management.jsp` | 1 |  
| `jsp/views/my-notifications-management.jsp` | 1 |  
| `html/send-notification.html` | 1 |  
| `html/notifications.html` | 1 |  
  
## File peggiori (violano più categorie)  
  
- `send-notification-management.jsp` → tutti e 3  
- `my-notifications-management.jsp` → tutti e 3  
- `notifications-management.jsp` → style tag + inline  
- `roles-management.jsp` → inline + script  
- `send-notification.html` → inline + script  
  
## Nota  
  
I wireframe in `splash/project/` contengono anch'essi `<style>`/inline/script, ma sono  
file di design statici — da confermare se vanno toccati o ignorati.