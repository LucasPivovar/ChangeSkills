import { ref, watch } from 'vue'
import { globalLocales } from './locales/global'
import { homeLocales } from './locales/home'
import { schoolLocales } from './locales/school'
import { coursesLocales } from './locales/courses'
import { contactLocales } from './locales/contact'
import { studentLocales } from './locales/studentArea'
import { ingles50Locales } from './locales/ingles50plus'

// Set reactive current language, defaulting to PT or stored user choice
export const currentLang = ref(localStorage.getItem('selectedLanguage') || 'pt')

// Watch for changes and save to localStorage
watch(currentLang, (newLang) => {
  localStorage.setItem('selectedLanguage', newLang)
})

const locales = {
  global: globalLocales,
  home: homeLocales,
  school: schoolLocales,
  courses: coursesLocales,
  contact: contactLocales,
  student: studentLocales,
  ingles50: ingles50Locales
}

/**
 * Resolves a value from a nested object using dot-notation.
 * e.g. resolvePath({a: {b: 'hello'}}, 'a.b') => 'hello'
 */
function resolvePath(obj, path) {
  if (!obj || !path) return undefined
  const parts = path.split('.')
  let current = obj
  for (const part of parts) {
    if (current == null || typeof current !== 'object') return undefined
    current = current[part]
  }
  return typeof current === 'string' || Array.isArray(current) ? current : undefined
}

/**
 * Natively translates a key based on active current language.
 * Falls back to PT, then to the key itself if not found.
 * Supports dot-notation for nested keys (e.g. 'teacherNames.paula', 'espanhol.jovensTitle').
 * 
 * @param {string} key - Dictionary key to look up (supports dot-notation)
 * @param {string} section - Target dictionary section file name
 */
export function t(key, section = 'global') {
  const lang = currentLang.value
  const sectionData = locales[section]
  if (!sectionData) return key

  // Try current language first, then fall back to 'pt', then return the key itself
  const resolved =
    resolvePath(sectionData[lang], key) ??
    resolvePath(sectionData['pt'], key) ??
    key

  return resolved
}
