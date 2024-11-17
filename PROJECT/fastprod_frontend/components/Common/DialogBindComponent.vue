<template>
  <UiDialog
    ref="ref"
    :width="width"
    :header="{
      icon: header.icon,
      label: header.label,
    }"
  >
    <template #content>
      <v-container>
        <slot name="header"></slot>
        <component
          :is="component"
          v-if="!!component"
          :data="componentProps"
          @event="$emit('event', null)"
          @onSubmit="onSubmit"
        ></component>
      </v-container>
    </template>
  </UiDialog>
</template>

<script>
export default {
  props: {
    component: {
      type: String,
      default: null,
    },
    componentProps: {
      type: Object,
      default: null,
    },
    width: {
      type: String,
      default: "800",
    },
    header: {
      type: Object,
      default: () => ({ icon: null, label: null }),
    },
  },
  methods: {
    open() {
      this.$refs.ref.open();
    },
    close() {
      this.$refs.ref.close();
    },
    onSubmit(e) {
      this.$emit("onSubmit", e);
    },
  },
};
</script>
